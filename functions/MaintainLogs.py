
import datetime

def maintain_logs(func):
    def inner(*args,**kwargs):
        print(f"Function {func.__name__} called at {datetime.datetime.now()}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished at {datetime.datetime.now()}")
        return result
    return inner
        


@maintain_logs
def paymentprocess(amount):
    for i in range(1,1000000):
        pass
    print(f"Processing payment of {amount} units.")

@maintain_logs
def sendMail(to,subject):
    print(f"Sending email to {to} with subject '{subject}'.")


paymentprocess(100)
sendMail("ok@gmail.com", "Test Subject")    

