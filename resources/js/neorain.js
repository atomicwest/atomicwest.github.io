var container;
	//this variable helps determine where on the screen the objects start from
	var ishort = 90;
	var canvas;
	var stage;
	var count = 0;
	var backgroundmain;
	
	function init(){
		canvas = document.getElementById("raincan")
		stage = new createjs.Stage(canvas);
		
		/*
		//create a black backdrop for the animation
		backgroundmain = new createjs.Shape();
		//backgroundmain.graphics.beginFill("black").drawRect(0,0,canvas.width, canvas.height);
		//manually adding the canvas dimensions declared at the bottom
		backgroundmain.graphics.beginFill("black").drawRect(-10,-10,8000, 3000);
		stage.addChild(backgroundmain);
		stage.update();
		*/
		var titlemain = new createjs.Text("Atomic West", "bold 90px Verdana", "#fff")
		titlemain.textBaseline = "bottom"
		titlemain.textAlign = "center"
		//stage.addChild(titlemain);
		//stage.update();
		
		//var gradient = ['#e5f2ff','#cce5ff','#99ccff','#66b2ff','#3399ff','#007fff','#0066cc','#004c99','#003366','#000d1a'];
		var gradient = ['#99ccff','#cce5ff', '#007fff', '#00ccff',
			'#66e0ff','#1a8cff','#4d4dff','	#007fff','#1ac6ff','#4da6ff']
		for (var i=1; i<30; i++){
			
			var rdrop = new createjs.Shape();
			var rcolsph = gradient[Math.floor(Math.random()*gradient.length)];
			rdrop.graphics.beginRadialGradientFill(["#fff",rcolsph,"rgba(0,0,0,0)"],
			[0,0,1], 25,25,2,25,25,20)
			rdrop.graphics.drawCircle(25,25,20);
			
			rdrop.x = Math.floor(Math.random()*canvas.width);
			//rdrop.y = Math.floor(Math.random()*canvas.height);
			rdrop.y = -200;
			
			//control speed with these values
			rdrop.velx = Math.random()*5;
			rdrop.vely = 1+Math.random()*5;
			rdrop.snapToPixel = true;
			
			//uncomment for diamond shape, blue custom gradient
			/*
			var drop = new createjs.Shape();
			for(var v=gradient.length; v>0; v--){
				//uncomment for dark core gradient to light border
				//drop.graphics.beginFill(gradient[gradient.length-v]);
				//uncomment for light core gradient to dark border
				drop.graphics.beginFill(gradient[v]);
				drop.graphics.moveTo(30-1.5*v,30+3*v).lineTo(40,20-3*v).lineTo(50+1.5*v,30+3*v).lineTo(40,100+5*v).lineTo(30-1.5*v,30+3*v);
			}
			*/
		/*
			var randtxt = new createjs.Text("Icicle Drop", "bold 13px italic", "#66ffc2" );
			randtxt.x = 40;
			randtxt.y = 25;
		*/
		
			container = new createjs.Container();
			container.addChild(rdrop);
			//container.x = 140;
			//container.y = 20;
			container.x = Math.floor(Math.random()*canvas.width);
			container.y = Math.floor(Math.random()*canvas.height);
			//container.y = 0;
			
			container.velx = Math.random() * 10 - 4;
			container.vely = 1+Math.random() * 10 - 4;
			//not sure if snapToPixel is an attribute for container?
			container.snapToPixel = true;
			
			/*
			createjs.Tween.get(container, {loop: true})				
				//endx = container.x + Math.floor(Math.random()*10);
				endy = container.y + Math.floor(Math.random()*200);
				.to({alpha:0,y: endy },1000)
			*/
			//createjs.Ticker.setFPS(200);
			
			toggleCache(true);
			
			createjs.Ticker.timingMode = createjs.Ticker.RAF;
			createjs.Ticker.addEventListener("tick",tick);	
			
			//stage.addChild(container);
			stage.addChild(rdrop, titlemain);
			stage.update();
			
		};
		
		stage.update();
	
	}
	
	function tick(event){
		var w = canvas.width + ishort * 2;
		var h = canvas.height + ishort *2;
		var l = stage.getNumChildren()-1;
		console.log(stage.getNumChildren())
		
		//iterate through the number of children
		//vary their velocities based on shape attributes defined in init()
		for (var i=1; i<l; i++){
				var shape = stage.getChildAt(i+1);
				shape.x = (shape.x + ishort + shape.velx + w) % w - ishort;
				shape.y = (shape.y + ishort + shape.vely + h) % h - ishort +1 ;
				
			};
		
		
		stage.update(event);
	}
	
	function toggleCache(value){
		var l = stage.getNumChildren()-11;
		
		for (var i=1; i<l; i++){
			var shape = stage.getChildAt(i);
			if(value){
				shape.cache(-ishort*2, -ishort, ishort*2, ishort*2);
			}
			else{
				shape.uncache();
			}
		}
	
	}
	