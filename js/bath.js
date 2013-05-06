/* start enchant */
enchant();

window.onload = function () {
	var game = new Game(500, 400);
	game.fps = 30;
	game.scale = 1;

	/* preload background and bubbles */
	game.preload(
		'img/bath/bg.png',
		'img/bath/bubble.png',
		'img/bath/sponge.png',
		'img/bath/sparkle.png',
		'img/bath/donebutton.png'
	);

	/* preload pet images depending on which pet is selected */
	// TODO: make this prettier
	switch(getCookie("pet_type")) {
		case "testpet":
		game.preload(
			'img/testpet/testpet_normal.png',
			'img/testpet/testpet_happy.png'
		);
		break;

		case "testpet2":
		game.preload(
			'img/testpet2/testpet2_normal.png',
			'img/testpet2/testpet2_happy.png'
		);
		break;

		default:
		console.log("ERROR: Could not detect which pet is selected.");
		break;
	}

	game.onload = function () {
		var scene = new SceneGame();
		game.pushScene(scene);
	};
	game.start();  
};

/* get cookie function */
function getCookie(c_name)
{
	var c_value = document.cookie;
	var c_start = c_value.indexOf(" " + c_name + "=");
		if (c_start == -1)
		  {
		  c_start = c_value.indexOf(c_name + "=");
		  }
		if (c_start == -1)
		  {
		  c_value = null;
		  }
		else
		  {
		  c_start = c_value.indexOf("=", c_start) + 1;
		  var c_end = c_value.indexOf(";", c_start);
		  if (c_end == -1)
		  {
		c_end = c_value.length;
		}
		c_value = unescape(c_value.substring(c_start,c_end));
		}
	return c_value;
}