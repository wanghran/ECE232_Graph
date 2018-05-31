library('igraph')
wc <- cluster_fast_greedy(graph)
x<-communities(wc)
writeLines(unlist(lapply(x, paste, collapse=" ")),"outfile.txt")