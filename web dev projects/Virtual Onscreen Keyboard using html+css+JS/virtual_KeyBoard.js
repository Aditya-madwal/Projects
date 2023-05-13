console.log('hello');

console.log("virtual keyboard !!!")
    buttons = document.querySelectorAll('button');

// let screenValue = '';
screen = document.getElementById('screen');
for (item of buttons) {
    item.addEventListener('click', (e) => {
        buttonText = e.target.innerText;
        console.log('Button text is ', buttonText);
        screen.value += buttonText;
    })}
document.getElementById('space').addEventListener('click',function name() {
    console.log("you pressed"+' ')
    screen.value += " ";
})