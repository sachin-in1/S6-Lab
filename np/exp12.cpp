#include <stdio.h>

int main(){
int count,src_router,i,j,k,w,v,min;
int cost_matrix[100][100],dist[100],last[100];
int flag[100];
printf("\nEnter the number of routers: ");
scanf("%d",&count);
printf("\nEnter the cost matrix values: \n");
for(i=1;i<=count;i++){
for(j=1;j<=count;j++){
scanf("%d",&cost_matrix[i][j]);
if(cost_matrix[i][j]<0)
cost_matrix[i][j]=1000;
}
}
printf("\nEnter the source router: ");
scanf("%d",&src_router);
for(v=1;v<=count;v++){
flag[v]=0;
last[v]=src_router;
dist[v]=cost_matrix[src_router][v];
}
flag[src_router]=1;
for(i=1;i<=count;i++){
min=1000;
for(w=1;w<=count;w++){
if(!flag[w])
if(dist[w]<min){
v=w;
min=dist[w];
}
}
flag[v]=1;
for(w=1;w<=count;w++){if(!flag[w])
if(min+cost_matrix[v][w]<dist[w]){
dist[w]=min+cost_matrix[v][w];
last[w]=v;
}
}
}
for(i=1;i<=count;i++){
printf("\n%d==>%d:\n\tPath taken:%d",src_router,i,i);
w=i;
while(w!=src_router){
printf("<--%d",last[w]);
w=last[w];
}
printf("\n\tShortest path cost:%d ",dist[i]);
}
}
