#exec &> logfile.txt

timestamp() {
    date +"[%Y-%m-%d %H:%M:%S] Running all scripts..."
}

while true
do
    timestamp
    for f in *.py; do python "$f"; echo "running $f"; done
    sleep 300
done
