for (let i=1;i<100;i++){
    var zeros = '0'.repeat(5-String(i).length)
    var key = zeros+String(i)
    console.log(key)
}