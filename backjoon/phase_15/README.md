### 백트래킹

- Promising : 트리 구조를 기반으로 DFS로 깊이 탐색을 진행하면서 각 루트에 대해 조건에 부합하는지 체크한다.
- Pruning: 해당 트리에서 조건에 맞지 않는 노드는 더 이상 DFS로 깊이 탐색을 진행하지 않고 가지치기를 한다.

### 백트래킹 구현
- 해를 구하는 도중 해가 아니어서 막히면 막히기 전으로 다시 돌아가서 해를 찾는 기법
- 예를 들어, 갈랫길에서 한쪽으로 갔다가 이 길이 아닌 것 같으면 왔던 길로 되돌아와 다른 선택지로 간다.
- 가상의 트리에서 해를 구하기 위해 부모 노드에서 자식 노드까지 뻗어나간다. 만약 해당 노드가 조건에 맞지 않는다면 다시 부모노드로 돌아간다.
- 해가 아닌 선택지는 없애면서 탐색하기 때문에 시간복잡도를 줄일 수 있다.


