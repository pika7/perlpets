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
	var cookieArray = getCookie("ID").split("&");
	var petType = cookieArray[0];

	game.preload(
		'img/' + petType + '/' + petType + '_normal.png',
		'img/' + petType + '/' + petType + '_happy.png'
	);

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