init python in telemetry:
    
    import urllib, urllib2, json

    def init():

        global host, project_id, game_id, collected_data, sessions, last_session_length, session_blocks, status

        if not renpy.store.is_telemetry_allowed:
            return

        host = "http://192.241.146.97:3000/v1/" #"http://localhost:3000/v1/" #
        project_id = "FoundersLifeAlpha"
        game_id = ""

        collected_data = {}

        sessions = 1
        last_session_length = 0
        session_blocks = []
        status = ""

    def setup():
        """
        Start the actual syncing process in a thread so the game doesn't hang.
        """

        if not renpy.store.is_telemetry_allowed:
            return
        renpy.invoke_in_thread(_setup)

    def _setup():
        """
        Queries the server to generate a game id that will be used for saving game data.
        """

        global game_id, status
    
        import platform

        status = "setup"
        os = platform.system()
        resolution = str((renpy.display.get_info().current_w, renpy.display.get_info().current_h))
        render = renpy.get_renderer_info()["renderer"]

        if not check_internet():
            game_id = "placeholder"
            status = ""

            return "No Internet connection."

        payload = {
            "project_id": project_id,
            "platform": "placeholder", #os,
            "display_render": "placeholder", #render,
            "display_size": "0, 0", #resolution,
            "multiple_ids": "False" #renpy.store.persistent.multiple_id
        }

        data = json.dumps(payload)

        r = urllib2.Request(host + project_id, data, { "Content-Type": "application/json" })
        response = urllib2.urlopen(r)

        # Get the game ID. It will idenitfy the game play
        game_id = response.read()[1:-1]
        print game_id.encode("utf-8")

        # Now mark it so that we know if a player is playing the game multiple times.
        renpy.store.persistent.multiple_id = True

        # Reset the status so that other functions can proceed as required.
        status = ""

    def collect():
        global collected_data, status

        if not renpy.store.is_telemetry_allowed:
            return

        # If some other operation is taking place, wait.
        while status:
            continue

        # Set the status to mark that we are in an operation
        status = "collecting"
        week = renpy.store.week
        print game_id.encode("utf-8")

        # If for some reason no game_id has been generated, generate one.
        if game_id == "placeholder":
            setup()

            # If we are able to connect to internet and get a id, copy all the needed data
            if game_id != "placeholder":
                collected_data[game_id] = collected_data["placeholder"]
                del collected_data["placeholder"]

        collected_data[week] = {
            "week": week,
            "energy": renpy.store.energy,
            "productivity": renpy.store.productivity,
            "mindfulness": renpy.store.morale,
            "cashflow": renpy.store.money,
            "points_earned": renpy.store.founder_score
        }
        status = ""

    def sync():
        """
        Start the actual syncing process in a thread so the game doesn't hang.
        """

        # Save the collected data and url locally since we are in a different thread now and
        # the collected_data dict can change while we are syncing.

        if not renpy.store.is_telemetry_allowed:
            return

        while status:
            continue

        if game_id == "placeholder":
            setup()
            return

        url = host + project_id + "/" + game_id + "/"
        renpy.invoke_in_thread(_sync, available_data=collected_data, url=url)

    def _sync(available_data, url):

        global status
        status = "syncing"

        if not check_internet():
            return "No Internet Connection"

        for entry, data in available_data.items():
            data = json.dumps(data)

            try:
                r = urllib2.Request(url, data, { "Content-Type": "application/json" })
                response = urllib2.urlopen(r)
            except Exception, e:
                return "No Internet Connection"

            # When two choices are placed back to back and player fast clicks + skips through them,
            # the entry will be removed but it's reference will remain in one of the threads.
            try:
                del collected_data[entry]
            except KeyError:
                pass

        status = ""

    def check_internet():
        """
        Returns True if Internet connection is present, otherwise, returns False
        """

        try:
            urllib2.urlopen(host, timeout=10)
            return True
        except urllib2.URLError:
            return False

    def resume():
        global sessions, last_session_length, session_blocks

        if not renpy.store.is_telemetry_allowed:
            return

        sessions += 1
        last_session_length = renpy.get_game_runtime() - last_session_length
        session_blocks.append(last_session_length)

    def end(name):

        if not renpy.store.is_telemetry_allowed:
            return

        if game_id == "placeholder":
            setup()
            return

        # Save the url locally since we are in a different thread now
        url = host + project_id + "/" + game_id + "/end/"
        play_time = renpy.get_game_runtime()
        session = sessions
        session_blocks.append(play_time - last_session_length)
        
        renpy.invoke_in_thread(_end, name=name, play_time=play_time, session=session, url=url)

    def _end(name, play_time, session, url):
        data = {
            "ending": name,
            "total_points": renpy.store.total_founder_score,
            "play_time": play_time,
            "sessions": session,
            "sessions_length": session_blocks,
            "days": renpy.store.total_days
            }

        data = json.dumps(data)

        try:
            r = urllib2.Request(url, data, { "Content-Type": "application/json" })
            response = urllib2.urlopen(r)
        except Exception, e:
            return "No Internet Connection"
        status = ""

    def submit_form():
        """
        Start the actual syncing process in a thread so the game doesn't hang.
        """
        
        if not renpy.store.is_telemetry_allowed:
            return

        while status:
            continue

        if game_id == "placeholder":
            setup()
            return

        url = host + project_id + "/" + game_id + "/form"
        renpy.invoke_in_thread(_submit_form, available_data=renpy.store.feedback, url=url)

    def _submit_form(available_data, url):
        global status

        status = "syncing"

        if not check_internet():
            return "No Internet Connection"

        data = json.dumps(available_data)

        try:
            r = urllib2.Request(url, data, { "Content-Type": "application/json" })
            response = urllib2.urlopen(r)
        except Exception, e:
            print str(e)
            return "No Internet Connection"
