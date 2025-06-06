This template gives you a more "complete" dashboard for exploring the tips dataset. For an overview of what's here, visit [this article](https://shiny.posit.co/py/docs/user-interfaces.html).


shiny run dashboard-tips/app.py \
    -h 127.0.0.1 -p 8000 --launch-browser \
    --reload  --app-dir . 


lsof -i :8000
kill -9 <PID>
