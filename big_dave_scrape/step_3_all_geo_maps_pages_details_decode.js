
var ss =  null
for (var ys, zs = "", As = 0; 174 > As; ++As)
    zs += String.fromCharCode(3 ^ "eRiRG`12oe1yfqyryIPhPq,fyjd1{EdriQY`S:WtiPKB6MFL[eqRnhliKjhWT{n(LV:PR;Li2O{R#DKqYpndO0e{wdoGwKEsiW[iMRkGlg1p0,SZkpTL:{7onh6auK2IeuFbrhbsN7u(Gdr[uUz2tWhkW#wKjgW1yp,Q,RQ;fU2Od\x3e".charCodeAt(As));
for (var Bs = zs, Cs = [], Ds = 0, Es = 0; Es < Bs.length; Es++) {
    for (var Fs = Bs.charCodeAt(Es); 255 < Fs; )
        Cs[Ds++] = Fs & 255,
        Fs >>= 8;
    Cs[Ds++] = Fs
}
ys = Cs;

function davidrumseySux(a) {
        if (!sa(a))
            return a;
        var b = a;
        try {
            var c = Pf(a);
            if (!sa(c))
                return c;
            b = c
        } catch (p) {}
            var d = us(b)
              , e = new ps;
            e.xl(ys);
            var f;
            f || (f = d.length);
            var g = e.wn
              , h = e.xn
              , l = e.c;
            for (a = 0; a < f; ++a) {
                var g = g + 1 & 255
                  , h = h + l[g] & 255
                  , m = l[g];
                l[g] = l[h];
                l[h] = m;
                d[a] ^= l[l[g] + l[h] & 255]
            }
            e.wn = g;
            e.xn = h;
            var n;
            if (8192 >= d.length)
                n = String.fromCharCode.apply(null, d);
            else {
                e = "";
                for (f = 0; f < d.length; f += 8192)
                    e += String.fromCharCode.apply(null, fb(d, f, f + 8192));
                n = e
            }
            return Qf(n)

    }

    function sa(a) {
        return "string" == typeof a
    }

    function ta(a) {
        return "number" == typeof a
    }

    function ua(a) {
        return "function" == pa(a)
    }

    function va(a) {
        var b = typeof a;
        return "object" == b && null != a || "function" == b
    }

    function wf(a) {
        return "vertical" == a ? "goog-slider-vertical" : "goog-slider-horizontal"
    }
    ;
    function Of(a) {
        return /^\s*$/.test(a) ? !1 : /^[\],:{}\s\u2028\u2029]*$/.test(a.replace(/\\["\\\/bfnrtu]/g, "@").replace(/(?:"[^"\\\n\r\u2028\u2029\x00-\x08\x0a-\x1f]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)[\s\u2028\u2029]*(?=:|,|]|}|$)/g, "]").replace(/(?:^|:|,)(?:[\s\u2028\u2029]*\[)+/g, ""))
    }
    function Pf(a) {
        a = String(a);
        if (Of(a))
            try {
                return eval("(" + a + ")")
            } catch (b) {}
        throw Error("Invalid JSON string: " + a);
    }
    function Qf(a) {
        return eval("(" + a + ")")
    }
    ;function Rf(a) {
        if (a.rc && "function" == typeof a.rc)
            return a.rc();
        if (sa(a))
            return a.split("");
        if (ra(a)) {
            for (var b = [], c = a.length, d = 0; d < c; d++)
                b.push(a[d]);
            return b
        }
        return mb(a)
    }
    function Sf(a, b, c) {
        if (a.forEach && "function" == typeof a.forEach)
            a.forEach(b, c);
        else if (ra(a) || sa(a))
            G(a, b, c);
        else {
            var d;
            if (a.Ec && "function" == typeof a.Ec)
                d = a.Ec();
            else if (a.rc && "function" == typeof a.rc)
                d = void 0;
            else if (ra(a) || sa(a)) {
                d = [];
                for (var e = a.length, f = 0; f < e; f++)
                    d.push(f)
            } else
                d = nb(a);
            for (var e = Rf(a), f = e.length, g = 0; g < f; g++)
                b.call(c, e[g], d && d[g], a)
        }
    }
    ;function Tf(a, b) {
        this.a = {};
        this.ra = [];
        this.X = 0;
        var c = arguments.length;
        if (1 < c) {
            if (c % 2)
                throw Error("Uneven number of arguments");
            for (var d = 0; d < c; d += 2)
                this.set(arguments[d], arguments[d + 1])
        } else
            a && this.addAll(a)
    }
    function us(a) {
        var b = [];
        vs(a, function(a) {
            b.push(a)
        });
        return b
    }

    function ps() {
        this.c = [];
        this.xn = this.wn = 0
    }
    ps.prototype.xl = function(a, b) {
        b || (b = a.length);
        for (var c = this.c, d = 0; 256 > d; ++d) c[d] = d;
        for (var e = 0, d = 0; 256 > d; ++d) {
            var e = e + c[d] + a[d % b] & 255,
                f = c[d];
            c[d] = c[e];
            c[e] = f
        }
        this.xn = this.wn = 0
    };

    function vs(a, b) {
        function c(b) {
            for (; d < a.length;) {
                var c = a.charAt(d++),
                    e = ts[c];
                if (null != e) return e;
                if (!/^[\s\xa0]*$/.test(c)) throw Error("Unknown base64 encoding at char: " + c);
            }
            return b
        }
        ws();
        for (var d = 0;;) {
            var e = c(-1),
                f = c(0),
                g = c(64),
                h = c(64);
            if (64 === h && -1 === e) break;
            b(e << 2 | f >> 4);
            64 != g && (b(f << 4 & 240 | g >> 2), 64 != h && b(g << 6 & 192 | h))
        }
    }
    function ws() {
        if (!ss) {
            ss = {};
            ts = {};
            for (var a = 0; 65 > a; a++)
                ss[a] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/\x3d".charAt(a),
                ts[ss[a]] = a,
                62 <= a && (ts["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.".charAt(a)] = a)
        }
    }
function fb(a, b, c) {
    return 2 >= arguments.length ? Array.prototype.slice.call(a, b) : Array.prototype.slice.call(a, b, c)
}


var fs = require('fs');
var glob = require("glob")

glob("/Volumes/Lately/dave_scrape/dave_maps/*.json", {}, function (er, files) {



  files.forEach((f)=>{
  	console.log(f)

  	var data = JSON.parse(fs.readFileSync(f, 'utf8'));


  	fs.appendFileSync('output.ndjson', JSON.stringify(davidrumseySux(data['geoData'])) + '\n');


  })


})



// 
// var data = JSON.parse(fs.readFileSync('dave_scrape_with_dave_data.json', 'utf8'));


// data.forEach((d)=>{

//     if (d.daveData){
//         d.daveData.geoDataDecoded = davidrumseySux(d.daveData.geoData)
//     }
// })



// fs.writeFileSync('dave_data_final.json', JSON.stringify(data,null,2));




