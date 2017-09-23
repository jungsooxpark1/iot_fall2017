var process = require('process');
var writeFile = require('write-file');
var a = 0;

var questions =[
	"What is your name?",
	"Are you a navy or pirate?"
];

var answers = [];

function ask(i){
	process.stdout.write(`\n\n ${questions[i]}`);
	process.stdout.write(": ");
}

process.stdin.on('data',function(data){

	answers.push(data.toString().trim());

	if(answers.length < questions.length){
		ask(answers.length);
	} else{
		writeFile('week3hw/iknow.txt', "Dear " + answers[0] + "," +'\n\n'+ "I know you. You are a " + answers[1] + "." +'\n'+ "I won't tell anyone about this because we are good friends." +'\n'+ "Hope you have a good day."+'\n\n'+"See you in another life, brother!"+'\n\n\n'+ "Sincerely," +'\n'+ "yourPi", function (err) {
  	if (err) return console.log(err);
  		else {console.log('\n\n $$$ Check your Pi $$$');
  		a = 1;
  		}
	});

		if(a == 1) process.exit();

	}
});



ask(0);
