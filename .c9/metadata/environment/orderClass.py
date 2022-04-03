{"filter":false,"title":"orderClass.py","tooltip":"/orderClass.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":49,"column":40},"end":{"row":49,"column":41},"action":"remove","lines":["t"],"id":866,"ignore":true},{"start":{"row":49,"column":40},"end":{"row":49,"column":41},"action":"insert","lines":["w"]}],[{"start":{"row":50,"column":38},"end":{"row":50,"column":39},"action":"remove","lines":["t"],"id":867,"ignore":true},{"start":{"row":50,"column":38},"end":{"row":50,"column":39},"action":"insert","lines":["w"]}],[{"start":{"row":48,"column":37},"end":{"row":48,"column":38},"action":"remove","lines":["t"],"id":868,"ignore":true}],[{"start":{"row":48,"column":37},"end":{"row":48,"column":38},"action":"insert","lines":["w"],"id":869,"ignore":true}],[{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"remove","lines":["t"],"id":870,"ignore":true},{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"insert","lines":["w"]}],[{"start":{"row":57,"column":10},"end":{"row":67,"column":80},"action":"remove","lines":["if(ask.get(price)):","            existing = bid.get(price)[0]","            if(newOrd.side == \"bid\"):","               newOrders.append(('M',netOrd.volume+ existing.volume,existing)) ","            elif(existing.volume > netOrd.volume):","                newOrders.append(('M',netOrd.volume - existing.volume,existing)) ","            elif(existing.volume == netOrd.volume):","                newOrders.append(('C', 0,existing)) ","            else:","                newOrders.append(('C', 0,existing)) ","                newOrders.append(('A',netOrd.volume-existing.volume,netOrders)) "],"id":871,"ignore":true},{"start":{"row":57,"column":10},"end":{"row":67,"column":80},"action":"insert","lines":["if(bid.get(price)):","            existing = bid.get(price)[0]","            if(newOrd.side == \"bid\"):","               newOrders.append(('M',newOrd.volume+ existing.volume,existing)) ","            elif(existing.volume > newOrd.volume):","                newOrders.append(('M',newOrd.volume - existing.volume,existing)) ","            elif(existing.volume == newOrd.volume):","                newOrders.append(('C', 0,existing)) ","            else:","                newOrders.append(('C', 0,existing)) ","                newOrders.append(('A',newOrd.volume-existing.volume,netOrders)) "]}],[{"start":{"row":70,"column":36},"end":{"row":70,"column":37},"action":"remove","lines":["t"],"id":872,"ignore":true},{"start":{"row":70,"column":36},"end":{"row":70,"column":37},"action":"insert","lines":["w"]}],[{"start":{"row":59,"column":31},"end":{"row":59,"column":34},"action":"remove","lines":["bid"],"id":873,"ignore":true},{"start":{"row":59,"column":31},"end":{"row":59,"column":32},"action":"insert","lines":["a"]}],[{"start":{"row":59,"column":32},"end":{"row":59,"column":34},"action":"insert","lines":["sk"],"id":874,"ignore":true}],[{"start":{"row":58,"column":23},"end":{"row":58,"column":26},"action":"remove","lines":["bid"],"id":875,"ignore":true},{"start":{"row":58,"column":23},"end":{"row":58,"column":24},"action":"insert","lines":["a"]}],[{"start":{"row":58,"column":24},"end":{"row":58,"column":26},"action":"insert","lines":["sk"],"id":876,"ignore":true}],[{"start":{"row":57,"column":13},"end":{"row":57,"column":16},"action":"remove","lines":["bid"],"id":877,"ignore":true},{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"insert","lines":["a"]}],[{"start":{"row":57,"column":14},"end":{"row":57,"column":16},"action":"insert","lines":["sk"],"id":878,"ignore":true}],[{"start":{"row":67,"column":80},"end":{"row":68,"column":12},"action":"remove","lines":["","            "],"id":879,"ignore":true}],[{"start":{"row":54,"column":80},"end":{"row":55,"column":16},"action":"remove","lines":["","                "],"id":880,"ignore":true}],[{"start":{"row":32,"column":0},"end":{"row":33,"column":29},"action":"remove","lines":["    bid1,ask1 = insOrderBook1","    bid2,ask2 = indOrderBook2"],"id":881,"ignore":true}],[{"start":{"row":30,"column":0},"end":{"row":67,"column":59},"action":"remove","lines":["def reviseOrderBook(insOrderBook1,insOrderBook2,netOrders):","    ","","    newOrders = []","    ","    for l in newOrders:","        newOrd = netOrders[l]","        ins,price = l","        if(ins == \"PHILIP_A\"):","            bid,ask = insOrderBook1","        else:","            bid,ask = insOrderBook2","    ","        if(bid.get(price)):","            existing = bid.get(price)[0]","            if(newOrd.side == \"bid\"):","               newOrders.append(('M',newOrd.volume+ existing.volume,existing)) ","            elif(existing.volume > newOrd.volume):","                newOrders.append(('M',newOrd.volume - existing.volume,existing)) ","            elif(existing.volume == newOrd.volume):","                newOrders.append(('C', 0,existing)) ","            else:","                newOrders.append(('C', 0,existing)) ","                newOrders.append(('A',newOrd.volume-existing.volume,netOrders)) ","                ","        elif(ask.get(price)):","            existing = ask.get(price)[0]","            if(newOrd.side == \"ask\"):","               newOrders.append(('M',newOrd.volume+ existing.volume,existing)) ","            elif(existing.volume > newOrd.volume):","                newOrders.append(('M',newOrd.volume - existing.volume,existing)) ","            elif(existing.volume == newOrd.volume):","                newOrders.append(('C', 0,existing)) ","            else:","                newOrders.append(('C', 0,existing)) ","                newOrders.append(('A',newOrd.volume-existing.volume,netOrders)) ","        else:","            newOrders.append(('A',newOrd.volume,netOrders))"],"id":882}],[{"start":{"row":11,"column":0},"end":{"row":28,"column":24},"action":"remove","lines":["def agreggateOrder(orderList):","        ","        netOrders = defaultdict(list)","        for x in orderList:","            if(not netOrders.get(x.instrument_id,x.price)):","                netOrders[(x.instrument_id,x.price)].append(x)","            else:","                y = netOrders.get(x.instrument_id,x.price)","                if (y.side == x.side):","                    y.volume += x.volume","                else:","                    if(y.side < x.side):","                        y.side = x.side","                        y.volume = x.volume-y.volume","                    else:","                        y.volume -= x.volume","        ","        return netOrders"],"id":883}],[{"start":{"row":8,"column":49},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":884},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]},{"start":{"row":9,"column":8},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "],"id":885}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["d"],"id":886},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["e"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":[" "],"id":887},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["_"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["_"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["s"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["t"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"remove","lines":["r"],"id":888}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["r"],"id":889},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["_"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["_"]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":17},"action":"insert","lines":["()"],"id":890}],[{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":[":"],"id":891}],[{"start":{"row":10,"column":18},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":892},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["s"],"id":893},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["e"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["l"]},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["f"]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["r"],"id":894},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["e"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["t"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["u"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["r"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":[" "],"id":895}],[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["w"],"id":896},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["s"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"remove","lines":["t"],"id":897},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"remove","lines":["s"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"remove","lines":["w"]}],[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["s"],"id":898},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["t"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["r"]}],[{"start":{"row":11,"column":18},"end":{"row":11,"column":20},"action":"insert","lines":["()"],"id":899}],[{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["s"],"id":900},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["e"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["l"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["f"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["."]}],[{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"insert","lines":["s"],"id":901},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["t"]},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":11,"column":24},"end":{"row":11,"column":27},"action":"remove","lines":["str"],"id":902},{"start":{"row":11,"column":24},"end":{"row":11,"column":32},"action":"insert","lines":["strategy"]}],[{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":[" "],"id":903},{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"insert","lines":["+"]}],[{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"insert","lines":[" "],"id":904},{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"insert","lines":["s"]},{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"remove","lines":["e"],"id":905}],[{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"insert","lines":["t"],"id":906},{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"insert","lines":["r"]}],[{"start":{"row":11,"column":39},"end":{"row":11,"column":41},"action":"insert","lines":["()"],"id":907}],[{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"insert","lines":["s"],"id":908},{"start":{"row":11,"column":41},"end":{"row":11,"column":42},"action":"insert","lines":["e"]},{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"insert","lines":["l"]},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"insert","lines":["f"]},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"insert","lines":["."]}],[{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"insert","lines":["i"],"id":909},{"start":{"row":11,"column":46},"end":{"row":11,"column":47},"action":"insert","lines":["n"]},{"start":{"row":11,"column":47},"end":{"row":11,"column":48},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":45},"end":{"row":11,"column":48},"action":"remove","lines":["ins"],"id":910},{"start":{"row":11,"column":45},"end":{"row":11,"column":58},"action":"insert","lines":["instrument_id"]}],[{"start":{"row":11,"column":59},"end":{"row":11,"column":60},"action":"insert","lines":[" "],"id":911}],[{"start":{"row":11,"column":60},"end":{"row":11,"column":61},"action":"insert","lines":["+"],"id":912}],[{"start":{"row":11,"column":61},"end":{"row":11,"column":62},"action":"insert","lines":[" "],"id":913},{"start":{"row":11,"column":62},"end":{"row":11,"column":63},"action":"insert","lines":["s"]},{"start":{"row":11,"column":63},"end":{"row":11,"column":64},"action":"insert","lines":["e"]},{"start":{"row":11,"column":64},"end":{"row":11,"column":65},"action":"insert","lines":["l"]},{"start":{"row":11,"column":65},"end":{"row":11,"column":66},"action":"insert","lines":["f"]},{"start":{"row":11,"column":66},"end":{"row":11,"column":67},"action":"insert","lines":["."]}],[{"start":{"row":11,"column":66},"end":{"row":11,"column":67},"action":"remove","lines":["."],"id":914},{"start":{"row":11,"column":65},"end":{"row":11,"column":66},"action":"remove","lines":["f"]},{"start":{"row":11,"column":64},"end":{"row":11,"column":65},"action":"remove","lines":["l"]},{"start":{"row":11,"column":63},"end":{"row":11,"column":64},"action":"remove","lines":["e"]}],[{"start":{"row":11,"column":63},"end":{"row":11,"column":64},"action":"insert","lines":["t"],"id":915},{"start":{"row":11,"column":64},"end":{"row":11,"column":65},"action":"insert","lines":["r"]}],[{"start":{"row":11,"column":65},"end":{"row":11,"column":67},"action":"insert","lines":["()"],"id":916}],[{"start":{"row":11,"column":66},"end":{"row":11,"column":67},"action":"insert","lines":["s"],"id":917},{"start":{"row":11,"column":67},"end":{"row":11,"column":68},"action":"insert","lines":["e"]},{"start":{"row":11,"column":68},"end":{"row":11,"column":69},"action":"insert","lines":["l"]},{"start":{"row":11,"column":69},"end":{"row":11,"column":70},"action":"insert","lines":["f"]},{"start":{"row":11,"column":70},"end":{"row":11,"column":71},"action":"insert","lines":["."]}],[{"start":{"row":11,"column":71},"end":{"row":11,"column":72},"action":"insert","lines":["p"],"id":918},{"start":{"row":11,"column":72},"end":{"row":11,"column":73},"action":"insert","lines":["r"]}],[{"start":{"row":11,"column":71},"end":{"row":11,"column":73},"action":"remove","lines":["pr"],"id":919},{"start":{"row":11,"column":71},"end":{"row":11,"column":76},"action":"insert","lines":["price"]}],[{"start":{"row":11,"column":77},"end":{"row":11,"column":78},"action":"insert","lines":[" "],"id":920},{"start":{"row":11,"column":78},"end":{"row":11,"column":79},"action":"insert","lines":["+"]}],[{"start":{"row":11,"column":79},"end":{"row":11,"column":80},"action":"insert","lines":[" "],"id":921},{"start":{"row":11,"column":80},"end":{"row":11,"column":81},"action":"insert","lines":["s"]},{"start":{"row":11,"column":81},"end":{"row":11,"column":82},"action":"insert","lines":["e"]},{"start":{"row":11,"column":82},"end":{"row":11,"column":83},"action":"insert","lines":["l"]}],[{"start":{"row":11,"column":82},"end":{"row":11,"column":83},"action":"remove","lines":["l"],"id":922},{"start":{"row":11,"column":81},"end":{"row":11,"column":82},"action":"remove","lines":["e"]}],[{"start":{"row":11,"column":81},"end":{"row":11,"column":82},"action":"insert","lines":["t"],"id":923},{"start":{"row":11,"column":82},"end":{"row":11,"column":83},"action":"insert","lines":["r"]}],[{"start":{"row":11,"column":83},"end":{"row":11,"column":85},"action":"insert","lines":["()"],"id":924}],[{"start":{"row":11,"column":84},"end":{"row":11,"column":85},"action":"insert","lines":["s"],"id":925},{"start":{"row":11,"column":85},"end":{"row":11,"column":86},"action":"insert","lines":["e"]},{"start":{"row":11,"column":86},"end":{"row":11,"column":87},"action":"insert","lines":["l"]},{"start":{"row":11,"column":87},"end":{"row":11,"column":88},"action":"insert","lines":["f"]}],[{"start":{"row":11,"column":88},"end":{"row":11,"column":89},"action":"insert","lines":["."],"id":926}],[{"start":{"row":11,"column":89},"end":{"row":11,"column":90},"action":"insert","lines":["V"],"id":927}],[{"start":{"row":11,"column":89},"end":{"row":11,"column":90},"action":"remove","lines":["V"],"id":928}],[{"start":{"row":11,"column":89},"end":{"row":11,"column":90},"action":"insert","lines":["v"],"id":929},{"start":{"row":11,"column":90},"end":{"row":11,"column":91},"action":"insert","lines":["o"]}],[{"start":{"row":11,"column":89},"end":{"row":11,"column":91},"action":"remove","lines":["vo"],"id":930},{"start":{"row":11,"column":89},"end":{"row":11,"column":95},"action":"insert","lines":["volume"]}],[{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":["+"],"id":931}],[{"start":{"row":11,"column":34},"end":{"row":11,"column":36},"action":"insert","lines":["\"\""],"id":932}],[{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"insert","lines":[","],"id":933}],[{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"insert","lines":[" "],"id":934}],[{"start":{"row":11,"column":64},"end":{"row":11,"column":70},"action":"insert","lines":["+\", \" "],"id":935}],[{"start":{"row":11,"column":88},"end":{"row":11,"column":94},"action":"insert","lines":["+\", \" "],"id":936}],[{"start":{"row":11,"column":113},"end":{"row":11,"column":119},"action":"insert","lines":["+\", \" "],"id":937}],[{"start":{"row":11,"column":119},"end":{"row":11,"column":120},"action":"insert","lines":["+"],"id":938}],[{"start":{"row":11,"column":120},"end":{"row":11,"column":121},"action":"insert","lines":["s"],"id":939},{"start":{"row":11,"column":121},"end":{"row":11,"column":122},"action":"insert","lines":["e"]},{"start":{"row":11,"column":122},"end":{"row":11,"column":123},"action":"insert","lines":["l"]},{"start":{"row":11,"column":123},"end":{"row":11,"column":124},"action":"insert","lines":["f"]},{"start":{"row":11,"column":124},"end":{"row":11,"column":125},"action":"insert","lines":["."]}],[{"start":{"row":11,"column":125},"end":{"row":11,"column":126},"action":"insert","lines":["s"],"id":940},{"start":{"row":11,"column":126},"end":{"row":11,"column":127},"action":"insert","lines":["i"]}],[{"start":{"row":11,"column":125},"end":{"row":11,"column":127},"action":"remove","lines":["si"],"id":941},{"start":{"row":11,"column":125},"end":{"row":11,"column":129},"action":"insert","lines":["side"]}],[{"start":{"row":11,"column":129},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":942},{"start":{"row":12,"column":0},"end":{"row":12,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["r"],"id":943},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["e"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["t"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["u"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["r"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":[" "],"id":944}],[{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["f"],"id":945}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["'"],"id":946},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["'"]}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["{"],"id":947},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["}"]}],[{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["{"],"id":948},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["}"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["{"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["}"]}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["["],"id":949}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":["["],"id":950}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["{"],"id":951},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["}"]}],[{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":[","],"id":952}],[{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":[","],"id":953}],[{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":[","],"id":954}],[{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"insert","lines":[","],"id":955}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":31},"action":"insert","lines":["self.strategy"],"id":956}],[{"start":{"row":12,"column":34},"end":{"row":12,"column":52},"action":"insert","lines":["self.instrument_id"],"id":957}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["s"],"id":958},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["t"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["r"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["("]}],[{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"insert","lines":[")"],"id":959}],[{"start":{"row":12,"column":60},"end":{"row":12,"column":75},"action":"insert","lines":["str(self.price)"],"id":960}],[{"start":{"row":12,"column":78},"end":{"row":12,"column":94},"action":"insert","lines":["str(self.volume)"],"id":961}],[{"start":{"row":12,"column":96},"end":{"row":12,"column":97},"action":"insert","lines":["{"],"id":962},{"start":{"row":12,"column":97},"end":{"row":12,"column":98},"action":"insert","lines":["}"]}],[{"start":{"row":12,"column":97},"end":{"row":12,"column":106},"action":"insert","lines":["self.side"],"id":963}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":10},"action":"insert","lines":["# "],"id":964}],[{"start":{"row":4,"column":57},"end":{"row":4,"column":58},"action":"insert","lines":["S"],"id":965}],[{"start":{"row":4,"column":72},"end":{"row":4,"column":73},"action":"insert","lines":["S"],"id":967}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":40},"end":{"row":11,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1648986685135,"hash":"b9f2250ded45062f509c715c780da755b5bb54e0"}