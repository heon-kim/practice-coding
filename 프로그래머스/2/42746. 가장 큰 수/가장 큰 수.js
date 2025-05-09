function solution(numbers) {
    var answer = '';
    const arr = numbers.map(item => item.toString())
    arr.sort((a, b)=>{
        if(a+b<b+a){
            return 1
        }else if(b+a<a+b){
            return -1
        }else{
            return 0
        }
    })
    if (arr[0] == '0'){
        return '0'
    }
    return arr.join("");
}