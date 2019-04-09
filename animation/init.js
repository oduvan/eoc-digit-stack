requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            animationTemplateName: 'animation',
            animation: function($expl, data){
                var checkioInput = data.in;
                if (!checkioInput){
                    return;
                }
                var stack = [];
                var s = 0;
                var $table = $expl.find("table");
                for (var i = 0; i < checkioInput.length; i++) {
                    var $tr = $("<tr></tr>");
                    var c = checkioInput[i];

                    if (c.lastIndexOf("PUSH", 0) === 0) {
                        var ch = c.split(" ")[1];
                        stack.push(ch);
                    }
                    else if (c === "POP") {
                        if (stack.length > 0) {
                            s += Number(stack.pop());
                        }
                    }
                    else {
                        if (stack.length > 0) {
                            s += Number(stack[stack.length - 1]);
                        }
                    }

                    $tr.append($("<td></td>").text(c));
                    $tr.append($("<td></td>").text(stack.join(",")));
                    $tr.append($("<td></td>").text(s));
                    $table.append($tr);
                }
            },
            functions: {
                js: 'digitStack',
                python: 'digit_stack'
            }
        });
        io.start();
    }
);
