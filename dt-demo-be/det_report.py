import json
import logging

modules = ["typo", "slang", "dup", "pdd", "spc"]

class DetReport:
    def __init__(self, app, did):
        self.app = app                      # Flask app: used for logging
        self.did = did                      # Document id: must be given
        self.dname = ""                     # Document name
        self.active_module = []             # Active module chosen from user
        self.module_count = {}              # Numbers of error detected from active module
        self.contents = ""                  # original contents
        self.contents_with_highlights = ""  # contents with highlighting of detected errors

    def setDname(self, dbconn):
        self.app.logger.info("class DetReport - setDname(): "
                            + "Fetching dname ...")
        query = f"SELECT dname FROM doc WHERE did = {self.did}; "
        try:
            cursor = dbconn.cursor()
            cursor.execute(query)
            query_result = cursor.fetchone()
            self.dname = query_result[0]
            cursor.close()
        except Exception as e:
            self.app.logger.error("class DetReport - setDname(): "
                                  + "Error fetching dname from database.")
            self.app.logger.error("class DetReport - setDname():",e)

    def setActiveModule(self, dbconn):
        self.app.logger.info("class DetReport - setActiveModule(): "
                            + "Fetching active modules ...")
        query = ("SELECT "
                 +", ".join(modules)
                 +f" FROM doc WHERE did = {self.did};")
        try:
            cursor = dbconn.cursor()
            cursor.execute(query)
            query_result = cursor.fetchall()
            for i, q_r in enumerate(query_result[0]):
                if q_r == 1:
                    self.active_module.append(modules[i])
            cursor.close()
        except Exception as e:
            self.app.logger.error("class DetReport - setActiveModule(): "
                                  + "Error fetching active modules from database.")
            self.app.logger.error("class DetReport - setActiveModule():",e)

    def setModuleCount(self, dbconn):
        self.app.logger.info("class DetReport - setModuleCount(): "
                            + "Fetching module counts ...")
        queries = []
        for m in self.active_module:
            query = ""
            if m == "dup":
                query = ("SELECT COUNT(*) FROM sprocessing "
                         +f"WHERE dup = true AND did = {self.did};")
            else:
                query = (f"SELECT CAST(SUM(JSON_LENGTH(JSON_KEYS({m}))) AS SIGNED) "
                        +f"FROM sprocessing WHERE did = {self.did};")
            queries.append(query)
        
        try:
            cursor = dbconn.cursor()

            for i, q in enumerate(queries):
                cursor.execute(q)
                query_result = cursor.fetchone()
                self.module_count[self.active_module[i]] = query_result[0]

            cursor.close()
        except Exception as e:
            self.app.logger.error("class DetReport - setModuleCount(): "
                                  + "Error fetching module count from database.")
            self.app.logger.error("class DetReport - setModuleCount():",e)

    def setContents(self, dbconn):
        self.app.logger.info("class DetReport - setContents(): "
                            + "Fetching original document contents ...")
        query = f"SELECT contents FROM doc WHERE did = {self.did}; "
        try:
            cursor = dbconn.cursor()
            cursor.execute(query)
            query_result = cursor.fetchone()
            self.contents = query_result[0]
            cursor.close()
        except Exception as e:
            self.app.logger.error("class DetReport - setContents(): "
                                  + "Error fetching contents from database.")
            self.app.logger.error("class DetReport - setContents():",e)

    def setContentsWithHighlights(self, dbconn):
        self.app.logger.info("class DetReport - setDname(): "
                            + "Highlighting errors on original contents ...")
        contents = []
        max_sid = 1
        columns = ["sid", "did", "osent"] + modules + ["csent"]

        query = f"SELECT MAX(sid) FROM sprocessing WHERE did = {self.did}; "
        try:
            self.app.logger.info("class DetReport - setDname(): "
                                + "Fetching sentence indexes ...")
            cursor = dbconn.cursor()
            cursor.execute(query)
            query_result = cursor.fetchone()
            max_sid = query_result[0]
            cursor.close()
        except Exception as e:
            self.app.logger.error("class DetReport - setContentsWithHighlights():",e)

        for i in range(1, max_sid+1, 1):
            query = f"SELECT * FROM sprocessing WHERE did = {self.did} AND sid = {i}; "
            try:
                self.app.logger.info("class DetReport - setDname(): "
                                    + f"Fetching sentence #{i} ...")
                cursor = dbconn.cursor()
                cursor.execute(query)
                query_result = cursor.fetchall()

                osent = query_result[0][columns.index("osent")]

                csent = osent

                # Iterate every modules columns(index 3-7)
                for m in modules:
                    error_info = {}
                    value = query_result[0][columns.index(m)]
                    tag_st = f"<mark id='{m}'>"
                    tag_end = "</mark>"

                    # Duplication column stores different type of value
                    if m == "dup":
                        # Highlight whole sentence if value is 1
                        # For duplication column, True means duplication detected
                        if value == 1:
                            csent = tag_st+osent+tag_end
                    
                    # Confirm if error value exists
                    elif value is not None:
                        error_info = json.loads(value)

                        # Iterate error information if multiple errors from same module have been detected.
                        for i in error_info:
                            dvalue = error_info[i]["dvalue"]
                            csent = csent.replace(dvalue, tag_st+dvalue+tag_end)

                # Generated csent
                print(csent)
                contents.append(csent)
                # TODO: update table sprocessing column csent

                cursor.close()
            except Exception as e:
                self.app.logger.error("class DetReport - setContentsWithHighlights():",e)
        
        self.contents_with_highlights = "\n".join(contents)

    def fetchDetReportInfo(self,dbconn):
        self.setDname(dbconn)
        self.setActiveModule(dbconn)
        self.setModuleCount(dbconn)
        self.setContents(dbconn)
        self.setContentsWithHighlights(dbconn)

    def getDetReportInfo(self):
        self.app.logger.info("class DetReport - getDetReportInfo(): "
                            + "Detection report information has been requested.")
        info_dict = {"did": self.did,
                "dname": self.dname,
                "active_module": self.active_module,
                "module_count": self.module_count,
                "contents": self.contents,
                "contents_with_highlights": self.contents_with_highlights}
        info_json = ""
        try:
            info_json = json.dumps(info_dict, ensure_ascii=False)
        except Exception as e:
            self.app.logger.warning("class DetReport - getDetReportInfo(): "
                                  + "Json auto generation failed.")
            self.app.logger.warning("class DetReport - getDetReportInfo(): "
                                  + "Trying to create Json result.")
            info_json = "{"
            for key, value in info_dict.items():
                info_json += f'"{key}": "{value}",'
            info_json = info_json.rstrip(',') 
            info_json += '}'
        self.app.logger.info("class DetReport - getDetReportInfo(): "
                            + "Returning detection report information.")
        return info_json