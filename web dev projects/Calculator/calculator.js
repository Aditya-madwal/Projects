console.log('This is a Calculator');


// to evaluate the inputed value

document.getElementById('equals').addEventListener('click',function Solve() {
      let x = document.getElementById("screen").value
      let y = eval(x)
      document.getElementById("screen").value = y
})

let buttons = document.querySelectorAll('button');

let screen = document.getElementById('screen');
buttons = document.querySelectorAll('button');

let screenValue = '';

for (item of buttons) {
    item.addEventListener('click', (e) => {
        buttonText = e.target.innerText;
        console.log('Button text is ', buttonText);
        if (buttonText == 'X') {
            buttonText = '*';
            screenValue = buttonText;
            screen.value += screenValue;
          }else if (buttonText == 'AC') {
            screen.value = " "
          }else if (buttonText == 'Copy') {
            console.log("copy");
            document.getElementById('screen').select();
            document.execCommand("copy");
            alert('Result Copied Successfull !!!')
          }else if (buttonText == '='){
            // screen.value += buttonText;
            let x = document.getElementById("screen").value
            let y = eval(x)
            document.getElementById("screen").value = y
          }else {
            screen.value += buttonText;
          }
})}
