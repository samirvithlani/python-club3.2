def private_access(role):
    
    logs=[]
    def access():
        logs.append(role)
        if role =="ADMIN":
            return f"private access granted"
        else:
            return f"Access Denied"
    def accss_logs():
        return logs
    
    return access,accss_logs


access,logs = private_access("ADMIN")
print(access())
print(logs())

    