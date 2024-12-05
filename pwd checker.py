import tkinter as tk
window = tk.Tk()
window.title("Password Checker")
window.geometry("500x400")
label = tk.Label(window,text=" Enter password to check strength ")
label.pack(pady = 50)
text_box = tk.Text(window, height=1, width=30)
text_box.pack(pady=10)
def password_checker():
    password = text_box.get("1.0", tk.END).strip()
    n=len(password)
    d={}
    d['lower']=False
    d['upper']=False
    d['num']=False
    d['symb']=False
    for i in password:
        if 96<ord(i)<123:
            d['lower']=True
        elif 64<ord(i)<91:
            d['upper']=True
        elif 47<ord(i)<58:
            d['num']=True
        else:
            d['symb']=True
    time=0
    if d['lower'] :
        no_of_com=26**n
        p_t=no_of_com/1000000000
        time=time+p_t
    if d['upper']:
        no_of_com=26**n
        p_t=no_of_com/1000000000
        time=time+p_t
    if d['num']:
        no_of_com=10**n
        p_t=no_of_com/1000000000
        time=time+p_t
    if d['symb'] :
        no_of_com=33**n
        p_t=no_of_com/1000000000
        time=time+p_t
    def convert_seconds(seconds):
        # Constants for time units
        SECONDS_IN_MINUTE = 60
        SECONDS_IN_HOUR = 3600
        SECONDS_IN_DAY = 86400
        SECONDS_IN_YEAR = 31536000  # Approximate number of seconds in a year

    # Determine the appropriate unit and convert
        if seconds < SECONDS_IN_MINUTE:
            return f"your password is very weak, it takes {seconds} seconds to crack"
        elif seconds < SECONDS_IN_HOUR:
            minutes = seconds / SECONDS_IN_MINUTE
            return f"your password weak, it takes {minutes:.2f} minutes to crack"
        elif seconds < SECONDS_IN_DAY:
            hours = seconds / SECONDS_IN_HOUR
            return f"your password is good, it takes {hours:.2f} hours to crack"
        elif seconds < SECONDS_IN_YEAR:
            days = seconds / SECONDS_IN_DAY
            return f"your password is Hard, it takes {days:.2f} days to crack"
        else:
            years = seconds / SECONDS_IN_YEAR
            return f"your password is very hard , it takes{years:.2f} years to crack"
    res=convert_seconds(time)
    output_label.config(text=f" {res}")
output_label = tk.Label(window, text="")
output_label.pack(pady=10)
bt = tk.Button(window,text= "check", command = password_checker)
bt.pack(pady=10)

window.mainloop()
