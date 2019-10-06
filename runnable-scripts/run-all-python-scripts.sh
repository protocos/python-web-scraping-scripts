exec &> logfile.txt

timestamp_begin() {
    date +"[%Y-%m-%d %H:%M:%S] Running all scripts..."
}

timestamp_end() {
    date +"[%Y-%m-%d %H:%M:%S] Run complete."
    sleep 60
}

while true
do
    timestamp_begin
    git pull
    sh dependencies.sh
    for f in scrape-*.py; do echo "running $f..."; python "$f"; done
    timestamp_end
done
