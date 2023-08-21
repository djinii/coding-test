function solution(num_list, n) {
    var answer = [];
    const len = num_list.length
    for (var i = 0; i<len; i++){
        if(i==0 || i % n == 0){
            answer.push(num_list[i])
        }
    }
    return answer;
}