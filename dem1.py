





esult = {   "full_url":"cfull_url",
            "p_resource":"cresource",
            "request":"crequest",
            "resource_type":"cresource_type"
    }


columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in esult.keys())
values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in esult.values())
sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
print(sql)
