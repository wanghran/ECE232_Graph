library(igraph)
G <- read.graph("../output/edge_list.txt",format="ncol",directed=FALSE)
feat <- read.csv('../output/feat_list.txt', header=TRUE, sep='|')
G <- set_vertex_attr(G, 'display_name', index=V(G), value=as.character(feat$name))
G <- set_vertex_attr(G, 'location', index=V(G), value=as.character(feat$coordinate))
group <- decompose.graph(G)
new_G <- group[[1]]
triangle_list <- triangles(new_G)
node_sample <- seq(1, length(triangle_list), 3)
node_list <- sample(node_sample, 1000)
triangle_ineq <- function(e1, e2, e3) {
    if ((e1 + e2 > e3) && (e2 + e3 > e1) && (e1 + e3 > e2))  {
        return (1)
    }else {
        return (0)
    }
}
count = 0
for (i in node_list) {
    edge <- E(new_G)
    x <- V(new_G)[triangle_list[i]]$name
    y <- V(new_G)[triangle_list[i + 1]]$name
    z <- V(new_G)[triangle_list[i + 2]]$name
    e1 <- get.edge.ids(new_G, vp=c(x, y))
    e2 <- get.edge.ids(new_G, vp=c(x, z))
    e3 <- get.edge.ids(new_G, vp=c(y, z))
    e1_len <- edge[e1]$weight
    e2_len <- edge[e2]$weight
    e3_len <- edge[e3]$weight
    count = count + triangle_ineq(e1_len, e2_len, e3_len)
}
percentage <- count / 1000.0
writeLines(format(percentage, digits=2),"../output/percentage.txt")