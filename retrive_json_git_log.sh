#!/bin/bash
# By: Douglas Anderson
# Borrowed by: https://gist.github.com/textarcana/1306223
# With hard coded directories. Sloppy but fast.

OUTFILE="/home/douglas/devel/git_stats/log.json"

cd ~/devel/school
git log --pretty=format:'{%n  "commit": "%H",%n  "parent": "%P",%n  "author": "%an <%ae>",%n  "date": "%ai",%n  "message": "%s%b"%n},' $@ | \
    perl -pe 'BEGIN{print "["}; END{print "]\n"}' | \
    perl -pe 's/},]/}]/' > $OUTFILE
cd -
echo "Done. Output to $OUTFILE"

