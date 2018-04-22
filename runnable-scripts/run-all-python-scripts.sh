exec &> logfile.txt

timestamp_begin() {
    date +"[%Y-%m-%d %H:%M:%S] Running all scripts..."
}

timestamp_end() {
    date +"[%Y-%m-%d %H:%M:%S] Run complete. Sleeping for 60 seconds"
    sleep 60
}

git pull
while true
do
    timestamp_begin
    git pull
    for f in scrape-*.py; echo "running $f"; do python "$f"; done
    timestamp_end
done
