// \servers\nodejs\sample.js

//const basics = require( '../common/libraries/basics.js' );

var blinkstick = require('blinkstick'),
    device = blinkstick.findFirst();

if (device) {
    var finished = false;

    device.blink('red', {'delay':100, 'repeats': 5}, function() {
        device.blink('green', {'delay':50, 'repeats': 10}, function() {
            device.blink('blue', {'delay':25, 'repeats': 20}, function() {
                finished = true;
            });
        });
    });

    var wait = function () { if (!finished) setTimeout(wait, 100)}
    wait();
}

//console.log( basics.COLORS.GRN1 + "HELLO" + basics.COLORS.NON0 );
