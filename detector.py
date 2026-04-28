def is_vulnerable(response):
  
    errors = [
        "you have an error in your sql syntax",
        "warning: mysql_fetch_array()",
        "unclosed quotation mark after the character string",
        "check the manual that corresponds to your mariadb server",
        "quoted string not properly terminated",
        "check the manual that corresponds to your mariadb server",
        "near ''''' at line 1",
        "sqlite3.operationalerror"
        
    ]
    
    content = response.text.lower()
    for error in errors:
        if error in content:
            return True
    return False

