init python:
    import json

    def decode(d):
        """
        This function decodes JSON data to proper Python Data. If required, it can be later expanded to serialise objects using custom fields and functions.
        """

        def correct(j):
            """
            Function for converting variables to their Python equivalent.
            """

            if isinstance(j, unicode):
                j = j.encode("utf-8").replace("\xc3\xa9", "é")

                if j == u"True":
                    j = True
                elif j == u"False":
                    j = False
                elif j == u"None":
                    j = None
                elif j.isdigit():
                    j = int(j)
                else:
                    try:
                        j = float(j)
                    except ValueError:
                        pass
            return j

        # In case the JSON data is enclosed in a list,
        # loop over it to extract the dict.
        if isinstance(d, _list):
            for e in d:
                decode(e)
            return d

        if isinstance(d, _dict):
            for i, k in d.iteritems():

                if isinstance(k, _dict):
                    decode(k)

                elif isinstance(k, _list):
                    for ind, ele in enumerate(k):
                        k[ind] = correct(ele)
                    d[i] = k
                    
                else:
                    d[i] = correct(k)

            return d

    def load(filepath, filename):
        try:
            data = decode(json.load(renpy.file("data/{}/{}.json".format(filepath, filename))))
        except IOError:
            return None

        return data
