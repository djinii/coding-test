function solution(array) {
    var answer = 0;
    array.sort((a, b) => a - b);
    const mid = Math.floor(array.length / 2);
    if (array.length % 2 === 0) {
        answer = (array[mid - 1] + array[mid]) / 2;
    } else {
        answer = array[mid];
    }
    return answer;
}