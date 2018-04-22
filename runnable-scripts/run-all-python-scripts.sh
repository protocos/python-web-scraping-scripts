exec &> logfile.txt

timestamp_begin() {
    date +"[%Y-%m-%d %H:%M:%S] Running all scripts..."
}

timestamp_end() {
    date +"[%Y-%m-%d %H:%M:%S] Run complete."
}

while true
do
    timestamp_begin
    git pull
    for f in scrape-*.py; do echo "running $f..."; python "$f"; done
    timestamp_end
done
