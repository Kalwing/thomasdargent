import { LeaderLine } from './leader-line.min.js';

var brevo_1 = document.getElementById('brevo-part-1');
var brevo_2 = document.getElementById('brevo-part-2');

window.onload = () => {
	setTimeout(() => {
		var line = new LeaderLine(brevo_1, brevo_2, { dash: true, color: '#17a1c5', path: 'fluid' });
		// line.setOptions({ startSocket: 'right' })
		line.startSocketGravity = [100, -10];
	}, 1000);
};
// var ld_1 = document.getElementById('ld-part-1')
// var ld_2 = document.getElementById('ld-part-2')
// setTimeout(() => {
// 	line = new LeaderLine(ld_1, ld_2, { dash: true, color: '#db8bc3', path: 'fluid' })
// 	line.setOptions({ startSocket: 'left' })
// 	line.startSocketGravity = [-130, 50]
// }, 300)
