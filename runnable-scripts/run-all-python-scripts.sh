while true
do
    echo "running all scripts"
    for f in *.py; do python "$f"; done
    sleep 300
done
