if [ $# -eq 0 ]
  then
    echo "Please specify filename"
	exit 1
fi
sox -d -c 1 "$1.wav" &
python3 /Users/rambo/capstone/buildKeylog.py $1
