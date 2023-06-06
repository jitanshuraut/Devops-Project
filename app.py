import psutil,datetime,time
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent(interval=1)
    mem_metric = psutil.virtual_memory().percent
    boot_time=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    cpu_count= psutil.cpu_count()
    proc_data=[]
    for proc in psutil.process_iter(['pid', 'name', 'username']):
     proc_data.append(proc.info)

    cpu_freq=psutil.cpu_freq(percpu=True)
    for data in cpu_freq:
        freq_data=data.current

    virtual_men=psutil.virtual_memory()
    p = psutil.Process()
    # mem_info=p.memory_info()
    disk=psutil.disk_usage('/')
    # net_con=psutil.net_connections()




    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
  
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message,boot_time=boot_time,cpu_count=cpu_count,cpu_freq=freq_data,virtual_men=virtual_men,disk=disk,proc_data=proc_data)
    #   time.sleep(1)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')