/*!
	reflection.js for jQuery v1.1
	(c) 2006-2011 Christophe Beyls <http://www.digitalia.be>
	MIT-style license.
*/
(function(b) {
    b.fn.extend({
        reflect: function(f) {
            f = b.extend({
                height: 1 / 3,
                opacity: 0.5
            }, f);
            var h, c = -1;
            "Microsoft Internet Explorer" == navigator.appName && null != /MSIE ([0-9]{1,}[.0-9]{0,})/.exec(navigator.userAgent) && (c = parseFloat(RegExp.$1));
            h = parseInt(c, 10);
            return this.unreflect().each(function() {
                var a = this;
                if (/^img$/i.test(a.tagName)) {
                    var c = function() {
                        var c = a.width,
                            g = a.height,
                            d, j, e, k;
                        j = Math.floor(1 < f.height ? Math.min(g, f.height) : g * f.height);
                        d = b("<canvas />")[0];
                        if (d.getContext) {
                            e = d.getContext("2d");
                            try {
                                b(d).attr({
                                    width: c,
                                    height: j
                                }), e.save(), e.translate(0, g - 1), e.scale(1, -1), e.drawImage(a, 0, 0, c, g), e.restore(), e.globalCompositeOperation = "destination-out", k = e.createLinearGradient(0, 0, 0, j), k.addColorStop(0, "rgba(255, 255, 255, " + (1 - f.opacity) + ")"), k.addColorStop(1, "rgba(255, 255, 255, 1.0)"), e.fillStyle = k, e.rect(0, 0, c, j), e.fill()
                            } catch (l) {
                                return
                            }
                        } else {
                            if (-1 == h) return;
                            d = b("<img />").attr("src", a.src).css({
                                width: c,
                                height: g,
                                marginBottom: j - g,
                                filter: "FlipV progid:DXImageTransform.Microsoft.Alpha(Opacity=" + 100 * f.opacity + ", FinishOpacity=0, Style=1, StartX=0, StartY=0, FinishX=0, FinishY=" + 100 * (j / g) + ")"
                            })[0]
                        }
                        b(d).css({
                            display: "block",
                            border: 0
                        });
                        d = b(/^a$/i.test(a.parentNode.tagName) ? "<span />" : "<div />").insertAfter(a).append([a, d])[0];
                        d.className = a.className;
                        b.data(a, "reflected", d.style.cssText = a.style.cssText);
                        b(d).css({
                            width: c,
                            height: g + j,
                            overflow: "hidden"
                        });
                        a.style.cssText = "display: block; border: 0px";
                        a.className = "reflected"
                    };
                    a.complete ? c() : b(a).load(c)
                }
            })
        },
        unreflect: function() {
            return this.unbind("load").each(function() {
                var f = b.data(this, "reflected"),
                    h;
                void 0 !== f && (h = this.parentNode, this.className = h.className, this.style.cssText = f, b.removeData(this, "reflected"), h.parentNode.replaceChild(this, h))
            })
        }
    })
})(jQuery);