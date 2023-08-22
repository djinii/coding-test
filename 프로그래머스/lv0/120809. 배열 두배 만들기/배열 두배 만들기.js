function solution(numbers) {
    var answer = [];
    //각 원소의 자신 값을 곱하고 answer배열에 넣기
    for(let i = 0; i<numbers.length; i++){
        answer.push(numbers[i] * 2)
    }
    return answer;
}