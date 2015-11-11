# StockRecommender
Recommend Stocks to Buy based on user actions (buy, sell, research)

1. Generate the simulated data
<br>  download log-synth: https://github.com/tdunning/log-synth
<br>  <b>~/log-synth-master/synth -schema trades.json -count $((1 * 10**6)) -format tsv -threads 1 -output trades</b>
<br> Note: change <b>trades.json</b> or increase/decrease count to make changes to simulated output

2. Parse the trade data
<br> <b>python metaData.py > index.json</b>
<br> note: the output of this file is ready to be loaded into elasticsearch
<br> <b>python prepareTrades.py > ml_input_file </b>
<br> note: the output of this script is a tab-delimited file which is ready for Mahout

3. Generate the significant co-occurrences
<br> <b>./genLogLikelihood</b>
<br> note: this runs the mahout item similarity and puts output in output/part-00000
<br> <b>python indicators.py > update.json</b>
<br> note: this prepares the file for updates into elasticsearch

4. Load and explore elasticsearch
<br> download elasticsearch: https://www.elastic.co/downloads/elasticsearch
<br> <b>cd ~/elasticsearch-X.X.X/</b>
<br> <b>./bin/elasticsearch </b> ### in new window ##
<br> <b>curl -XDELETE 'localhost:9200/finance/' </b> ## delete finance index if exists ##
<br> <b>curl -XPUT 'localhost:9200/finance'; echo</b> ## create index ###
<br> <b>curl -s -XPOST localhost:9200/_bulk --data-binary @index.json; echo</b> ## create docs ##
<br> <b>curl -s -XPOST localhost:9200/_bulk --data-binary @update.json; echo</b> ## update docs ##

5. Recommendations (Sense and UI)
<br>GET finance/stock/_search
<br>     { "query": { "match":{"indicators":"489 11695 100297"} } ,
<br>       "fields":["_id","name","symbol","sector","marketCap"] }

<br> open <b>demo.html</b> in browser and enter actions in search to generate real-time recommendations
