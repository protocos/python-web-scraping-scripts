exec &> logfile.txt

timestamp_begin() {
    date +"[%Y-%m-%d %H:%M:%S] Running all scripts..."
}

timestamp_end() {
    date +"[%Y-%m-%d %H:%M:%S] Run complete. Sleeping for 60 seconds"
    sleep 60
}

while true
do
    timestamp_begin
    for f in *.py; do python "$f"; echo "running $f"; done
    timestamp_end
done
