var SceneGame = Class.create(Scene, {
	cleanliness: 0, // how clean the pet is
	clean: false, // if the pet is clean
	doingDown: false, // if the pet is currently going down
	timer: 0, // the timer until done button appears
	cookieUpdated: false, // if the cleanliness cookie has been updated

	initialize: function (score) {
		/* just so that the button can access it? */
		scene = this;

		/* call superclass constructor */
		Scene.apply(this);

		/* access to the game instance */
		this.game = Game.instance;

		/* spawn background */
		this.background = new Sprite(500, 400);
		this.background.image = this.game.assets["img/bath/bg.png"];
		this.addChild(this.background);

		/* get the pet type from the cookie */
		var petType = getCookie("pet_type");

		/* display the pet in the center */
		this.pet = new Pet(100, 50, petType);
		this.addChild(this.pet);

		/* create the sponge but don't add it yet */
		this.sponge = new Sprite(100, 100);
		this.sponge.image = this.game.assets['img/bath/sponge.png'];

		/* create the done button but don't add it yet */
		this.doneButton = new DoneButton(150, 150);

		this.addEventListener('touchstart', this.startScrub);
		this.addEventListener('touchmove', this.scrub);
		this.addEventListener('touchend', this.stopScrub);
		this.addEventListener('enterframe', this.update);
	},

	update: function(evt) {
		if (this.cleanliness >= 300) {
			this.stopScrub();
			this.clean = true;
			this.pet.image = this.game.assets[this.pet.happyImage];
		}

		if (this.clean) {
			/* make the pet dance in happiness */
			/* hard code ALL THE THINGS!!! */
			if (this.pet.y <= 40) {
				this.goingDown = false;
			}
			else if (this.pet.y >= 60) {
				this.goingDown = true;
			}

			if (this.goingDown) {
				this.pet.y -= 5;
			}
			else {
				this.pet.y += 5;
			}

			/* spawn some random sparkles */
			if (Math.random() > 0.75) {
				this.addChild(new Sparkle(Math.random() * 350, Math.random() * 250));
			}

			/* increment timer */
			if (this.timer <= 2000) {
				this.timer += evt.elapsed;
			}
			else {
				/* show the done button and keep bringing it to the top */
				this.removeChild(this.doneButton);
				this.addChild(this.doneButton);

				if (!this.cookieUpdated) {
					this.cookieUpdated = true;
					// update the cleanliness cookie here
				}
			}
		}
	},

	startScrub: function(evt) {
		/* make the sponge show up */
		if (!this.clean) {
			this.sponge.x = evt.x - 50;
			this.sponge.y = evt.y - 50;
			this.addChild(this.sponge);
			this.pet.startScrub(evt);
		}
	},

	scrub: function(evt) {
		/* spawn a bubble */
		if (!this.clean) {
			if (Math.random() > 0.75) {
				this.addChild(new Bubble(evt.x - 75, evt.y - 75));
			}

			/* make the sponge follow the mouse and keep it on top */
			this.removeChild(this.sponge);
			this.addChild(this.sponge);
			this.sponge.x = evt.x - 50;
			this.sponge.y = evt.y - 50;
			this.pet.scrub(evt);

			this.cleanliness++; // make pet cleaner
		}
	},

	stopScrub: function(evt) {
		if (!this.clean) {
			/* hide the sponge */
			this.removeChild(this.sponge);
			this.pet.stopScrub(evt);
		}
	}
});

/* get cookie function, seriously, why i gotta copy and paste */
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

/* the pet in the center */
var Pet = Class.create(Sprite, {
	/* the x and y coordinates of the mouse in the last frame */
	lastMouseX: 0,
	lastMouseY: 0,

	initialize: function(x, y, petType) {
		/* call superclass constructor */
		Sprite.apply(this);

		/* access the game instance */
		this.game = Game.instance;

		this.x = x;
		this.y = y;
		this.width = 300;
		this.height = 300;
		this.petType = petType;
		this.normalImage = "img/" + this.petType + "/" + this.petType + "_normal.png";
		this.happyImage = "img/" + this.petType + "/" + this.petType + "_happy.png";

		this.image = this.game.assets[this.normalImage];
	},

	startScrub: function(evt) {
		/* save the position of the first mouse click */
		this.lastMouseX = evt.x;
		this.lastMouseY = evt.y;
	},

	scrub: function(evt) {
		this.image = this.game.assets[this.happyImage];

		/* move the pet slightly in the direction of the mouse */
		if (evt.x > this.lastMouseX) {
			this.x += 0.2;
		}
		else if (evt.x < this.lastMouseX) {
			this.x -= 0.2;
		}

		if (evt.y > this.lastMouseY) {
			this.y += 0.2;
		}
		else if (evt.y < this.lastMouseY) {
			this.y -= 0.2;
		}

		/* save the coordinates of the mouse */
		this.lastMouseX = evt.x;
		this.lastMouseY = evt.y;
	},

	stopScrub: function(evt) {
		this.image = this.game.assets[this.normalImage];
	}
});

/* soap bubble */
var Bubble = Class.create(Sprite, {
	initialize: function(x, y) {
		/* call superclass constructor */
		Sprite.apply(this);

		/* access the game instance */
		this.game = Game.instance;

		this.x = x;
		this.y = y;
		this.width = 150;
		this.height = 150;
		this.image = this.game.assets["img/bath/bubble.png"];
		this.frame = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, null];

		/* set a random rotation */
		this.rotation = Math.random() * 360;

		this.addEventListener('enterframe', this.update);
	},

	update: function(evt) {
		/* kill the bubble after it is done appearing */
		if (this.frame === 4) {
			this.remove();
		}
	}
});

/* sparkle */
var Sparkle = Class.create(Sprite, {
	initialize: function(x, y) {
		/* call superclass constructor */
		Sprite.apply(this);

		/* access the game instance */
		this.game = Game.instance;

		this.x = x;
		this.y = y;
		this.width = 150;
		this.height = 150;
		this.image = this.game.assets["img/bath/sparkle.png"];
		this.frame = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, null];

		this.addEventListener('enterframe', this.update);
	},

	update: function(evt) {
		/* kill the bubble after it is done appearing */
		if (this.frame === 5) {
			this.remove();
		}
	}
});

/* done button */
var DoneButton = Class.create(Sprite, {
	initialize: function(x, y) {
		/* call superclass constructor */
		Sprite.apply(this);

		/* access to the game instance */
		this.game = Game.instance;

		this.x = x;
		this.y = y;
		this.width = 200;
		this.height = 100;
		this.image = this.game.assets["img/bath/donebutton.png"];

		this.addEventListener('touchstart', this.closeWindow);
	},

	closeWindow: function(evt) {
		window.close();
	}
})