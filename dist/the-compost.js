function a0b(a, b) {
    const c = a0a();
    return a0b = function (d, e) {
        d = d - 0x174;
        let f = c[d];
        if (a0b['JdDspJ'] === undefined) {
            var g = function (l) {
                const m = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
                let n = '', o = '';
                for (let p = 0x0, q, r, s = 0x0; r = l['charAt'](s++); ~r && (q = p % 0x4 ? q * 0x40 + r : r, p++ % 0x4) ? n += String['fromCharCode'](0xff & q >> (-0x2 * p & 0x6)) : 0x0) {
                    r = m['indexOf'](r);
                }
                for (let t = 0x0, u = n['length']; t < u; t++) {
                    o += '%' + ('00' + n['charCodeAt'](t)['toString'](0x10))['slice'](-0x2);
                }
                return decodeURIComponent(o);
            };
            a0b['vdObdp'] = g, a = arguments, a0b['JdDspJ'] = !![];
        }
        const h = c[0x0], i = d + h, j = a[i];
        return !j ? (f = a0b['vdObdp'](f), a[i] = f) : f = j, f;
    }, a0b(a, b);
}
function a0a() {
    const n = [
        'Cg9ZAxrPB24',
        'yxbWzw5Kq2HPBgq',
        'twvZAa',
        'vMzzswS',
        'mJq2oty0oxjtteL1BG',
        'CMvUzgvY',
        'mty3otCZmK9WDLrdAW',
        'zMTuswq',
        'vMnbt1K',
        'ugvYC3bLy3rPDMvdyw1LCMe',
        'v2vIr0Xszw5KzxjLCG',
        'Aw5UzxjxAwr0Aa',
        'zg9TrwXLBwvUDa',
        'C2v0u2L6zq',
        'mtzNy3rrDue',
        'CM90yxrPB24',
        'yM9KEq',
        'mZG2mZjRquTHDuO',
        'qM94r2vVBwv0CNK',
        'ovbvtKfHwq',
        'mtq0mZv0wMTcs2m',
        'mtm3ntGWnKPMzNLcsW',
        'mty2mdG4odLJsevbs0q',
        'nZyYALfvCffq',
        'Aw5UzxjizwLNAhq',
        'mZnVy1fYCvi',
        'u2nLBMu',
        'ywrK',
        'twvZAejHC2LJtwf0zxjPywW',
        'ody2nZeWB2zNs1z6'
    ];
    a0a = function () {
        return n;
    };
    return a0a();
}
(function (a, b) {
    const k = a0b, c = a();
    while (!![]) {
        try {
            const d = -parseInt(k(0x183)) / 0x1 * (parseInt(k(0x17b)) / 0x2) + -parseInt(k(0x17f)) / 0x3 + parseInt(k(0x18e)) / 0x4 + parseInt(k(0x17e)) / 0x5 * (parseInt(k(0x181)) / 0x6) + -parseInt(k(0x18c)) / 0x7 * (parseInt(k(0x178)) / 0x8) + -parseInt(k(0x17d)) / 0x9 * (parseInt(k(0x187)) / 0xa) + parseInt(k(0x180)) / 0xb;
            if (d === b)
                break;
            else
                c['push'](c['shift']());
        } catch (e) {
            c['push'](c['shift']());
        }
    }
}(a0a, 0x63a66), ((() => {
    const l = a0b, a = {
            'VcAOY': function (i, j) {
                return i(j);
            },
            'VfYIk': function (i, j) {
                return i / j;
            },
            'fkTId': function (i) {
                return i();
            }
        }, b = new THREE[(l(0x184))](), c = new THREE[(l(0x191))](0x4b, a[l(0x18b)](window[l(0x175)], window[l(0x182)]), 0.1, 0x3e8), d = new THREE[(l(0x174))]();
    d[l(0x177)](window[l(0x175)], window[l(0x182)]), document[l(0x17a)][l(0x189)](d[l(0x176)]);
    const e = new THREE[(l(0x17c))](0x1, 0x1, 0x1), f = new THREE[(l(0x186))]({ 'color': 0xff00 }), g = new THREE[(l(0x18a))](e, f);
    b[l(0x185)](g), c[l(0x188)]['z'] = 0x5;
    function h() {
        const m = l;
        a[m(0x190)](requestAnimationFrame, h), g[m(0x179)]['x'] += 0.01, g[m(0x179)]['y'] += 0.01, d[m(0x18d)](b, c);
    }
    a[l(0x18f)](h);
})()));