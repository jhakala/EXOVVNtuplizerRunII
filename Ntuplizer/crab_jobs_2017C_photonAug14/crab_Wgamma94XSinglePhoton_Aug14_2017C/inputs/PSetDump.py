import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuple")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2017C/SinglePhoton/MINIAOD/31Mar2018-v1/90000/FE0443CC-A337-E811-881E-0CC47A7C351E.root'),
    lumisToProcess = cms.untracked.VLuminosityBlockRange( ("297050:12-297050:137", "297050:193-297050:776", "297056:12-297056:203", "297057:1-297057:4", "297057:14-297057:105", 
        "297057:112-297057:377", "297057:385-297057:418", "297057:424-297057:509", "297057:516-297057:906", "297099:24-297099:62", 
        "297100:1-297100:15", "297100:21-297100:369", "297100:375-297100:381", "297101:1-297101:668", "297101:673-297101:697", 
        "297101:700-297101:856", "297101:862-297101:937", "297101:943-297101:1101", "297113:1-297113:204", "297113:211-297113:252", 
        "297114:1-297114:99", "297114:106-297114:161", "297175:1-297175:85", "297176:11-297176:120", "297176:125-297176:214", 
        "297177:1-297177:162", "297178:1-297178:54", "297178:59-297178:334", "297178:342-297178:749", "297178:754-297178:967", 
        "297178:972-297178:1037", "297178:1043-297178:1264", "297178:1272-297178:1282", "297178:1290-297178:1385", "297215:1-297215:47", 
        "297218:1-297218:27", "297219:1-297219:80", "297219:85-297219:281", "297219:288-297219:579", "297219:585-297219:916", 
        "297219:921-297219:1429", "297219:1436-297219:2004", "297219:2010-297219:2638", "297224:10-297224:19", "297224:24-297224:138", 
        "297225:1-297225:32", "297227:9-297227:192", "297292:1-297292:125", "297292:130-297292:131", "297292:136-297292:667", 
        "297292:675-297292:753", "297293:1-297293:121", "297293:127-297293:150", "297296:1-297296:236", "297296:240-297296:401", 
        "297296:406-297296:418", "297296:425-297296:497", "297308:1-297308:44", "297359:39-297359:70", "297359:164-297359:180", 
        "297411:32-297411:737", "297411:740-297411:800", "297411:807-297411:950", "297424:32-297424:149", "297425:1-297425:107", 
        "297425:112-297425:157", "297426:1-297426:28", "297426:34-297426:84", "297426:90-297426:111", "297429:1-297429:72", 
        "297430:1-297430:199", "297431:1-297431:49", "297431:55-297431:64", "297431:71-297431:188", "297432:1-297432:112", 
        "297433:1-297433:159", "297434:1-297434:161", "297435:1-297435:94", "297467:50-297467:138", "297468:1-297468:74", 
        "297469:1-297469:4", "297469:9-297469:70", "297483:37-297483:68", "297483:71-297483:201", "297483:206-297483:214", 
        "297484:1-297484:47", "297484:53-297484:208", "297484:214", "297485:1-297485:16", "297485:23-297485:253", 
        "297485:258-297485:299", "297485:302-297485:314", "297485:321-297485:420", "297486:1-297486:74", "297486:79-297486:598", 
        "297486:603-297486:625", "297487:1-297487:433", "297487:439-297487:491", "297487:495-297487:603", "297487:609-297487:613", 
        "297488:1-297488:73", "297488:80-297488:424", "297503:5-297503:275", "297503:282-297503:559", "297503:566-297503:606", 
        "297503:612-297503:635", "297503:642-297503:772", "297503:777-297503:779", "297504:1-297504:41", "297504:125-297504:136", 
        "297505:1-297505:394", "297557:8-297557:28", "297557:67-297557:113", "297557:119-297557:167", "297557:173-297557:174", 
        "297557:180-297557:394", "297558:9-297558:266", "297562:1-297562:69", "297562:120-297562:369", "297563:1-297563:254", 
        "297563:260-297563:264", "297598:17", "297598:22-297598:33", "297599:1-297599:169", "297599:211-297599:225", 
        "297599:230-297599:312", "297599:319-297599:385", "297599:395-297599:407", "297603:1-297603:420", "297604:1-297604:126", 
        "297604:131-297604:272", "297604:279-297604:375", "297604:381-297604:407", "297605:1-297605:6", "297605:13-297605:20", 
        "297605:24-297605:89", "297605:95-297605:223", "297605:257-297605:407", "297606:1-297606:94", "297606:99-297606:231", 
        "297620:32-297620:318", "297656:64-297656:116", "297656:123-297656:135", "297656:140-297656:230", "297656:269-297656:307", 
        "297656:313-297656:330", "297656:341-297656:388", "297656:393-297656:433", "297665:1-297665:153", "297665:159-297665:209", 
        "297665:214-297665:279", "297666:1-297666:11", "297666:17-297666:81", "297666:86-297666:121", "297670:21-297670:34", 
        "297674:3-297674:102", "297674:108-297674:188", "297675:1-297675:123", "297675:129-297675:239", "297675:244-297675:328", 
        "297675:334-297675:467", "297675:470-297675:471", "297722:55-297722:160", "297722:165-297722:353", "297723:1-297723:13", 
        "297723:51-297723:222", "298996:33-298996:216", "298997:1-298997:37", "298997:47", "299000:4-299000:77", 
        "299042:33-299042:55", "299061:38-299061:355", "299062:1-299062:163", "299062:166-299062:303", "299064:7-299064:85", 
        "299065:13-299065:248", "299065:251-299065:342", "299067:1-299067:459", "299096:2-299096:97", "299149:29-299149:470", 
        "299178:37-299178:56", "299178:58-299178:111", "299180:5-299180:98", "299184:1-299184:561", "299185:1-299185:120", 
        "299327:1-299327:72", "299329:1-299329:172", "299368:37-299368:175", "299369:1-299369:303", "299370:1-299370:7", 
        "299370:47-299370:705", "299380:34-299380:227", "299381:1-299381:45", "299394:5-299394:33", "299395:1-299395:187", 
        "299396:1-299396:81", "299420:2-299420:50", "299443:145-299443:164", "299450:39-299450:88", "299477:39-299477:42", 
        "299477:82-299477:87", "299478:1-299478:175", "299479:1-299479:123", "299480:1-299480:6", "299480:8-299480:715", 
        "299481:1-299481:196", "299481:199-299481:236", "299481:260-299481:479", "299481:487-299481:940", "299481:943-299481:1037", 
        "299481:1061-299481:1257", "299593:95-299593:177", "299593:179-299593:896", "299594:1-299594:317", "299595:1-299595:134", 
        "299595:138", "299597:3-299597:91", "299597:93-299597:540", "299649:151-299649:332", "300087:36-300087:59", 
        "300087:61-300087:126", "300087:128-300087:216", "300087:218-300087:239", "300105:1-300105:21", "300106:1-300106:74", 
        "300107:1-300107:28", "300107:30-300107:47", "300117:35-300117:67", "300122:46-300122:730", "300122:735-300122:924", 
        "300122:927-300122:1295", "300123:1-300123:384", "300123:387-300123:612", "300155:35-300155:1229", "300156:1-300156:72", 
        "300157:9-300157:1107", "300226:43-300226:448", "300233:43-300233:162", "300234:1-300234:59", "300235:1-300235:187", 
        "300236:11-300236:187", "300237:1-300237:713", "300237:716-300237:717", "300238:30-300238:58", "300238:62-300238:329", 
        "300239:1-300239:145", "300239:148-300239:167", "300239:171-300239:213", "300240:1-300240:7", "300240:11-300240:46", 
        "300240:51-300240:362", "300280:52-300280:56", "300280:61-300280:69", "300280:73-300280:150", "300280:155-300280:165", 
        "300280:178-300280:198", "300280:207-300280:222", "300280:226-300280:251", "300280:255-300280:268", "300280:275-300280:345", 
        "300280:349-300280:370", "300280:381-300280:548", "300280:553-300280:607", "300280:617-300280:639", "300280:663-300280:691", 
        "300281:3-300281:8", "300282:1-300282:9", "300282:13-300282:59", "300282:73-300282:92", "300282:97-300282:114", 
        "300282:142-300282:151", "300282:156-300282:186", "300283:1-300283:34", "300284:1-300284:22", "300284:38-300284:47", 
        "300284:50-300284:82", "300284:90-300284:98", "300284:108-300284:130", "300284:133-300284:152", "300284:156-300284:250", 
        "300284:260-300284:414", "300284:420-300284:561", "300284:568-300284:585", "300284:590-300284:680", "300284:691-300284:751", 
        "300364:27-300364:46", "300365:1-300365:20", "300366:1-300366:21", "300367:1-300367:20", "300368:1-300368:20", 
        "300369:1-300369:20", "300370:1-300370:20", "300371:1-300371:20", "300372:1-300372:8", "300373:1-300373:21", 
        "300374:1-300374:21", "300375:1-300375:93", "300389:1", "300389:4-300389:5", "300389:8", 
        "300389:11-300389:20", "300389:23-300389:39", "300389:60-300389:149", "300390:2-300390:21", "300391:1-300391:21", 
        "300392:1-300392:21", "300393:1-300393:20", "300394:1-300394:21", "300395:1-300395:20", "300396:1-300396:20", 
        "300397:1-300397:20", "300398:1-300398:20", "300399:1-300399:20", "300400:1-300400:677", "300401:19-300401:673", 
        "300459:40-300459:332", "300461:1-300461:98", "300462:1-300462:97", "300463:1-300463:124", "300464:1-300464:103", 
        "300464:126-300464:265", "300466:1-300466:650", "300467:1-300467:563", "300497:26-300497:175", "300514:38-300514:150", 
        "300515:1-300515:838", "300515:957-300515:1013", "300516:1-300516:111", "300517:1-300517:8", "300517:103-300517:623", 
        "300558:8-300558:548", "300560:1-300560:640", "300560:645-300560:844", "300574:15-300574:111", "300575:1-300575:82", 
        "300576:7-300576:123", "300576:125-300576:1206", "300631:41-300631:49", "300631:63-300631:66", "300631:75-300631:226", 
        "300632:1-300632:21", "300633:1-300633:447", "300635:1-300635:23", "300635:26-300635:176", "300636:1-300636:335", 
        "300636:338-300636:1572", "300673:41-300673:47", "300673:49", "300673:52-300673:56", "300673:59-300673:66", 
        "300674:1-300674:33", "300675:1-300675:33", "300676:1-300676:26", "300742:56-300742:343", "300777:21-300777:509", 
        "300780:3-300780:341", "300785:1-300785:549", "300785:552-300785:750", "300785:752-300785:1201", "300785:1219-300785:1272", 
        "300806:36-300806:214", "300811:6-300811:508", "300812:1-300812:59", "300816:6-300816:161", "300817:1-300817:33", 
        "300817:36-300817:74", "300817:80-300817:383", "300817:410-300817:493", "301046:162-301046:223", "301141:25-301141:31", 
        "301142:1-301142:897", "301161:36-301161:805", "301165:1-301165:145", "301179:35-301179:59", "301180:1-301180:97", 
        "301183:3-301183:10", "301183:13-301183:303", "301281:38-301281:157", "301283:3-301283:886", "301298:45-301298:949", 
        "301323:35-301323:474", "301323:477-301323:990", "301330:22-301330:353", "301359:33-301359:319", "301384:1-301384:476", 
        "301391:38-301391:214", "301392:1-301392:627", "301393:2-301393:18", "301396:1-301396:33", "301397:1-301397:228", 
        "301397:231-301397:517", "301397:519-301397:728", "301398:1-301398:9", "301399:1-301399:108", "301417:50-301417:367", 
        "301447:86-301447:96", "301447:99-301447:400", "301447:404-301447:512", "301448:1-301448:329", "301449:1-301449:404", 
        "301450:1-301450:173", "301461:28-301461:581", "301472:35-301472:830", "301475:1-301475:18", "301476:1-301476:844", 
        "301519:42-301519:250", "301524:1-301524:110", "301524:117-301524:263", "301529:1-301529:49", "301530:1-301530:110", 
        "301531:1-301531:394", "301532:1-301532:611", "301567:14-301567:372", "301627:57-301627:943", "301664:28-301664:445", 
        "301665:1-301665:294", "301665:319-301665:487", "301694:36-301694:102", "301912:43-301912:52", "301912:101-301912:422", 
        "301913:1-301913:58", "301914:1-301914:350", "301941:31-301941:568", "301959:30-301959:1938", "301960:1-301960:147", 
        "301970:6-301970:123", "301984:17-301984:317", "301985:1-301985:367", "301986:1-301986:381", "301987:1-301987:1128", 
        "301997:37-301997:407", "301998:1-301998:1704", "302019:34-302019:86", "302026:24-302026:53", "302026:66-302026:72", 
        "302029:1-302029:98", "302031:1-302031:401", "302031:403-302031:446", "302031:448-302031:675", "302031:678-302031:818", 
        "302033:1-302033:40", "302033:44-302033:46", "302034:1-302034:20", "302037:18-302037:20", "302038:10", 
        "302040:1-302040:174", "302041:1-302041:72", "302042:1-302042:523", "302043:1-302043:228", "302131:71-302131:943", 
        "302159:33-302159:140", "302163:32-302163:671", "302163:674-302163:1230", "302165:1-302165:85", "302166:1-302166:16", 
        "302225:54-302225:133", "302225:136-302225:923", "302228:58-302228:78", "302228:81-302228:293", "302229:1-302229:457", 
        "302240:1-302240:960", "302262:37-302262:471", "302263:1-302263:1250", "302277:15-302277:17", "302277:22-302277:192", 
        "302277:194-302277:391", "302279:1-302279:71", "302280:1-302280:152", "302322:33-302322:870", "302328:42-302328:722", 
        "302337:27-302337:162", "302342:19-302342:72", "302343:1-302343:98", "302344:3-302344:482", "302350:1-302350:136", 
        "302388:27-302388:157", "302388:164-302388:717", "302392:45-302392:407", "302393:1-302393:887", "302448:21-302448:312", 
        "302448:317-302448:442", "302448:445-302448:483", "302448:486-302448:1926", "302472:28-302472:808", "302473:1-302473:368", 
        "302473:398-302473:406", "302474:1-302474:305", "302475:1-302475:7", "302476:1-302476:259", "302479:30-302479:222", 
        "302479:225-302479:340", "302484:8-302484:176", "302485:1-302485:922", "302492:10-302492:21", "302492:23-302492:59", 
        "302493:1-302493:7", "302494:1-302494:618", "302509:73-302509:92", "302513:37-302513:89", "302522:29-302522:46", 
        "302523:1-302523:59", "302525:1-302525:677", "302525:747-302525:778", "302526:1-302526:582", "302548:40-302548:124", 
        "302551:1-302551:7", "302553:1-302553:188", "302554:1-302554:7", "302555:1-302555:11", "302563:40-302563:46", 
        "302565:1-302565:7", "302572:6-302572:291", "302573:1-302573:693", "302573:730-302573:1285", "302596:47-302596:534", 
        "302596:545-302596:705", "302596:710-302596:986", "302597:1-302597:1054", "302634:37-302634:73", "302634:75-302634:123", 
        "302634:125-302634:129", "302634:133-302634:165", "302634:168-302634:175", "302634:177-302634:216", "302634:218-302634:358", 
        "302634:361-302634:375", "302634:378-302634:404", "302634:407-302634:423", "302634:425-302634:503", "302634:505-302634:578", 
        "302634:581-302634:594", "302634:596-302634:638", "302635:1-302635:22", "302635:24-302635:28", "302635:30-302635:39", 
        "302635:41-302635:53", "302635:55-302635:132", "302635:134-302635:144", "302635:146-302635:265", "302635:267-302635:271", 
        "302635:274-302635:344", "302635:347-302635:357", "302635:359-302635:375", "302635:378-302635:384", "302635:386-302635:414", 
        "302635:416-302635:494", "302635:497-302635:608", "302635:611-302635:634", "302635:637-302635:684", "302635:687-302635:706", 
        "302635:708-302635:724", "302635:726-302635:901", "302635:904-302635:954", "302635:957-302635:982", "302635:984-302635:1072", 
        "302635:1075-302635:1124", "302635:1126-302635:1129", "302635:1132-302635:1206", "302635:1209-302635:1234", "302635:1236-302635:1291", 
        "302651:1-302651:149", "302654:1-302654:317", "302661:1-302661:72", "302663:1-302663:706", "303825:1-303825:180", 
        "303832:54-303832:1334", "303832:1338-303832:1913", "303838:54", "303838:83-303838:2044", "303885:60-303885:2052", 
        "303948:55-303948:1678", "303998:58-303998:319", "303999:1-303999:751", "304000:1-304000:56", "304062:54-304062:2014", 
        "304119:71-304119:138", "304119:143-304119:150", "304120:1-304120:253", "304125:1-304125:1769", "304144:76-304144:2596", 
        "304144:2598-304144:2656", "304158:165-304158:1750", "304158:1752-304158:2087", "304169:50-304169:1714", "304169:1731-304169:1733", 
        "304170:1-304170:620", "304199:10-304199:18", "304200:1-304200:321", "304204:55-304204:607", "304209:52-304209:98", 
        "304209:100-304209:133", "304209:135-304209:157", "304209:176-304209:253", "304209:255-304209:477", "304291:56-304291:85", 
        "304292:1-304292:1125", "304292:1183-304292:1779", "304292:1781-304292:1811", "304333:74-304333:1653", "304354:82-304354:295", 
        "304366:44-304366:1387", "304366:1390-304366:1396", "304366:1399-304366:1402", "304366:1404-304366:1407", "304366:1409-304366:1412", 
        "304366:1414-304366:1416", "304366:1419-304366:1421", "304366:1424-304366:1873", "304446:40-304446:92", "304446:110-304446:111", 
        "304447:1-304447:534", "304447:540-304447:1644", "304451:1-304451:60", "304505:60-304505:86", "304506:1-304506:370", 
        "304507:1-304507:239", "304508:1-304508:1324", "304562:52-304562:56", "304562:60-304562:848", "304616:52-304616:223", 
        "304616:227-304616:740", "304616:747-304616:1002", "304625:73-304625:536", "304626:1-304626:8", "304654:53-304654:704", 
        "304655:1-304655:1194", "304661:53-304661:67", "304661:69-304661:143", "304661:147-304661:173", "304661:175-304661:198", 
        "304661:237-304661:240", "304662:1-304662:150", "304663:1-304663:689", "304671:51-304671:1193", "304672:1-304672:60", 
        "304737:69-304737:149", "304738:1-304738:1681", "304739:3-304739:16", "304740:1-304740:278", "304776:49-304776:98", 
        "304777:1-304777:431", "304777:438-304777:510", "304778:4-304778:1300", "304797:28-304797:87", "304797:91-304797:306", 
        "304797:308-304797:377", "304797:385-304797:1202", "304797:1205-304797:2950", "305044:3-305044:203", "305044:302-305044:306", 
        "305044:309-305044:310", "305044:313", "305044:318-305044:330", "305045:1-305045:873", "305046:1-305046:667", 
        "305046:671-305046:686", "305059:63-305059:518", "305059:520-305059:575", "305062:1-305062:8", "305063:1-305063:35", 
        "305064:1-305064:2045", "305081:52-305081:1107", "305112:68-305112:1527", "305113:9-305113:72", "305114:1-305114:526", 
        "305178:69-305178:124", "305179:1-305179:21", "305180:1-305180:9", "305181:1-305181:8", "305182:1-305182:8", 
        "305183:1-305183:231", "305183:262-305183:266", "305184:1-305184:8", "305186:1-305186:112", "305186:120-305186:422", 
        "305188:1-305188:1002", "305202:74-305202:132", "305202:136-305202:729", "305204:1-305204:1229", "305207:52-305207:1077", 
        "305208:1-305208:372", "305234:52-305234:99", "305236:1-305236:23", "305237:1-305237:16", "305237:18-305237:1147", 
        "305247:57-305247:433", "305248:1-305248:957", "305252:1-305252:548", "305282:75-305282:207", "305310:60-305310:157", 
        "305310:163-305310:458", "305311:1-305311:153", "305312:1-305312:227", "305313:1-305313:741", "305314:1-305314:404", 
        "305336:36-305336:241", "305338:1-305338:107", "305341:1-305341:503", "305349:1-305349:34", "305350:1-305350:21", 
        "305351:1-305351:868", "305358:91-305358:231", "305358:233-305358:253", "305364:50-305364:147", "305365:1-305365:668", 
        "305365:676-305365:832", "305366:1-305366:721", "305366:724-305366:756", "305366:769-305366:934", "305366:936-305366:1254", 
        "305376:71-305376:168", "305377:9-305377:1292", "305377:1294-305377:1383", "305377:1386-305377:1525", "305405:44-305405:536", 
        "305405:573-305405:575", "305406:1-305406:394", "305406:401-305406:520", "305406:528-305406:535", "305406:540-305406:1475", 
        "305440:20-305440:291", "305441:1-305441:121", "305516:46-305516:518", "305516:558-305516:639", "305517:1-305517:163", 
        "305518:1-305518:1134", "305586:53-305586:583", "305589:1-305589:691", "305590:1-305590:500", "305590:517-305590:1020", 
        "305636:60-305636:339", "305636:342-305636:667", "305636:671-305636:2390", "305766:55-305766:902", "305809:56-305809:197", 
        "305814:85-305814:689", "305814:692-305814:978", "305814:980-305814:1074", "305814:1077-305814:1912", "305821:59-305821:830", 
        "305832:87-305832:266", "305840:1-305840:1144", "305842:1-305842:862", "305862:81-305862:705", "305898:70-305898:780", 
        "305902:53-305902:521", "305967:1-305967:32", "306029:63-306029:96", "306030:1-306030:110", "306036:60-306036:63", 
        "306037:1-306037:49", "306038:1-306038:139", "306041:1-306041:320", "306042:1-306042:371", "306048:1-306048:140", 
        "306049:1-306049:358", "306051:1-306051:415", "306091:422-306091:629", "306092:1-306092:588", "306092:593-306092:976", 
        "306095:1-306095:300", "306121:57-306121:152", "306122:1-306122:127", "306125:1-306125:756", "306125:770-306125:2642", 
        "306125:2667-306125:3007", "306126:1-306126:497", "306134:53-306134:84", "306135:1-306135:1095", "306138:1-306138:1298", 
        "306139:1-306139:1112", "306153:78-306153:165", "306154:1-306154:251", "306154:253-306154:691", "306154:709-306154:1233", 
        "306155:1-306155:1440", "306169:1-306169:745", "306170:1-306170:22", "306171:1-306171:503", "306418:1-306418:33", 
        "306418:35-306418:75", "306419:1-306419:62", "306420:1-306420:108", "306422:9-306422:126", "306423:1-306423:333", 
        "306432:1-306432:339", "306454:13-306454:101", "306455:1-306455:11", "306456:1-306456:237", "306456:239-306456:787", 
        "306457:1-306457:31", "306458:1-306458:17", "306458:20-306458:35", "306458:37-306458:41", "306458:43-306458:47", 
        "306458:49-306458:53", "306458:56-306458:60", "306458:62-306458:66", "306458:68-306458:72", "306458:74-306458:77", 
        "306458:79-306458:83", "306458:85-306458:89", "306458:93-306458:102", "306458:104-306458:108", "306458:110-306458:114", 
        "306458:116-306458:120", "306458:122-306458:126", "306458:129-306458:139", "306458:141-306458:145", "306458:147-306458:151", 
        "306458:153-306458:166", "306458:169-306458:173", "306458:175-306458:179", "306458:181-306458:185", "306458:187-306458:191", 
        "306458:193-306458:197", "306458:200-306458:210", "306458:212-306458:216", "306458:218-306458:222", "306458:225-306458:229", 
        "306458:231-306458:235", "306458:237-306458:241", "306458:243-306458:247", "306458:249", "306458:252-306458:256", 
        "306458:258-306458:268", "306459:1-306459:512", "306459:514-306459:2275", "306460:1-306460:73" ) )
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.CondDBTauConnection = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497),
    HFdepthOneParameterB = cms.vdouble(-4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209),
    HFdepthTwoParameterA = cms.vdouble(0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593),
    HFdepthTwoParameterB = cms.vdouble(-2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06)
)

process.combinedSecondaryVertexCommon = cms.PSet(
    SoftLeptonFlip = cms.bool(False),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)

process.ghostTrackCommon = cms.PSet(
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.mvaEleID_Fall17_iso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml')
)

process.mvaEleID_Fall17_iso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz')
)

process.mvaEleID_Fall17_noIso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml')
)

process.mvaEleID_Fall17_noIso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz')
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Phys14NonTrig25nsV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2VariablesClassic.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring('-0.253', 
            ' 0.081', 
            '-0.081', 
            ' 0.965', 
            ' 0.917', 
            ' 0.683'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring('-0.483', 
            '-0.267', 
            '-0.323', 
            ' 0.933', 
            ' 0.825', 
            ' 0.337'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_Spring15_25ns_Trig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring15Trig25nsV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vstring('0.988153', 
            '0.96791', 
            '0.841729'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vstring('0.972153', 
            '0.922126', 
            '0.610764'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring15NonTrig25nsV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring(' 0.287435', 
            ' 0.221846', 
            '-0.303263', 
            ' 0.967083', 
            ' 0.929117', 
            ' 0.726311'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring('-0.083313', 
            '-0.235222', 
            '-0.67099', 
            ' 0.913286', 
            ' 0.805013', 
            ' 0.358969'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wpLoose = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring(' -0.265', 
            ' -0.556', 
            ' -0.551', 
            ' -0.072', 
            ' -0.286', 
            ' -0.267'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wpLoose'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_50ns_Trig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring15Trig50nsV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vstring('0.981841', 
            '0.946762', 
            '0.79704'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vstring('0.953843', 
            '0.849994', 
            '0.514118'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16GeneralPurposeV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16HZZV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
)

process.mvaPhoID_RunIIFall17_v1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
)

process.mvaPhoID_RunIIFall17_v1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
        mvaCuts = cms.vdouble(0.67, 0.54),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
        mvaCuts = cms.vdouble(0.27, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1p1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v1p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
)

process.mvaPhoID_RunIIFall17_v1p1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.67, 0.54),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.27, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v2'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz')
)

process.mvaPhoID_RunIIFall17_v2_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(0.42, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(-0.02, -0.26),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring15NonTrig25nsV2p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EE_V2.weights.xml.gz')
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.374, 0.336),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-25ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring15NonTrig50nsV2p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EE_V2.weights.xml.gz')
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.29538, 0.45837),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-50ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring16_nonTrig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring16NonTrigV1'),
    nCategories = cms.int32(2),
    phoIsoCutoff = cms.double(2.5),
    phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz')
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.softPFElectronCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)

process.softPFMuonCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trkIsol03CfgV2 = cms.PSet(
    barrelCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.3),
        maxDZ = cms.double(0.1),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    ),
    endcapCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.3),
        maxDZ = cms.double(0.5),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    )
)

process.variableJTAPars = cms.PSet(
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5)
)

process.c_vs_b_vars_vpset = cms.VPSet(cms.PSet(
    default = cms.double(-1),
    name = cms.string('vertexLeptonCategory'),
    taggingVarName = cms.string('vertexLeptonCategory')
), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSig_0'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip2dSig_1'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPPar_0'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPPar_1'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(0),
        name = cms.string('trackPParRatio_0'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(1),
        name = cms.string('trackPParRatio_1'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('jetNTracks'),
        taggingVarName = cms.string('jetNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexMass_0'),
        taggingVarName = cms.string('vertexMass')
    ), 
    cms.PSet(
        default = cms.double(-10),
        idx = cms.int32(0),
        name = cms.string('vertexEnergyRatio_0'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip2dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance2dSig_0'),
        taggingVarName = cms.string('flightDistance2dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance3dSig_0'),
        taggingVarName = cms.string('flightDistance3dSig')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexJetDeltaR_0'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(0),
        idx = cms.int32(0),
        name = cms.string('vertexNTracks_0'),
        taggingVarName = cms.string('vertexNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('massVertexEnergyFraction_0'),
        taggingVarName = cms.string('massVertexEnergyFraction')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexBoostOverSqrtJetPt_0'),
        taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonPtRel_0'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonPtRel_1'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(0),
        name = cms.string('leptonSip3d_0'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(1),
        name = cms.string('leptonSip3d_1'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonDeltaR_0'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonDeltaR_1'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatioRel_0'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatioRel_1'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonEtaRel_0'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonEtaRel_1'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatio_0'),
        taggingVarName = cms.string('leptonRatio')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatio_1'),
        taggingVarName = cms.string('leptonRatio')
    ))

process.c_vs_l_vars_vpset = cms.VPSet(cms.PSet(
    default = cms.double(-1),
    name = cms.string('vertexLeptonCategory'),
    taggingVarName = cms.string('vertexLeptonCategory')
), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSig_0'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip2dSig_1'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPPar_0'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPPar_1'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(0),
        name = cms.string('trackPParRatio_0'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(1),
        name = cms.string('trackPParRatio_1'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('jetNTracks'),
        taggingVarName = cms.string('jetNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexMass_0'),
        taggingVarName = cms.string('vertexMass')
    ), 
    cms.PSet(
        default = cms.double(-10),
        idx = cms.int32(0),
        name = cms.string('vertexEnergyRatio_0'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip2dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance2dSig_0'),
        taggingVarName = cms.string('flightDistance2dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance3dSig_0'),
        taggingVarName = cms.string('flightDistance3dSig')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexJetDeltaR_0'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(0),
        idx = cms.int32(0),
        name = cms.string('vertexNTracks_0'),
        taggingVarName = cms.string('vertexNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('massVertexEnergyFraction_0'),
        taggingVarName = cms.string('massVertexEnergyFraction')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexBoostOverSqrtJetPt_0'),
        taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonPtRel_0'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonPtRel_1'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(0),
        name = cms.string('leptonSip3d_0'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(1),
        name = cms.string('leptonSip3d_1'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonDeltaR_0'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonDeltaR_1'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatioRel_0'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatioRel_1'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonEtaRel_0'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonEtaRel_1'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatio_0'),
        taggingVarName = cms.string('leptonRatio')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatio_1'),
        taggingVarName = cms.string('leptonRatio')
    ))

process.mvaConfigsForEleProducer = cms.VPSet(cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Phys14NonTrig25nsV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2VariablesClassic.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring15NonTrig25nsV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring15Trig50nsV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring15Trig25nsV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16HZZV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16GeneralPurposeV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz')
    ))

process.mvaConfigsForPhoProducer = cms.VPSet(cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring15NonTrig50nsV2p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EE_V2.weights.xml.gz')
), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring15NonTrig25nsV2p1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EE_V2.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring16NonTrigV1'),
        nCategories = cms.int32(2),
        phoIsoCutoff = cms.double(2.5),
        phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v1p1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v2'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz')
    ))

process.puppiCentral = cms.VPSet(cms.PSet(
    algoId = cms.int32(5),
    applyLowPUCorr = cms.bool(True),
    combOpt = cms.int32(0),
    cone = cms.double(0.4),
    rmsPtMin = cms.double(0.1),
    rmsScaleFactor = cms.double(1.0),
    useCharged = cms.bool(True)
))

process.puppiForward = cms.VPSet(cms.PSet(
    algoId = cms.int32(5),
    applyLowPUCorr = cms.bool(True),
    combOpt = cms.int32(0),
    cone = cms.double(0.4),
    rmsPtMin = cms.double(0.5),
    rmsScaleFactor = cms.double(1.0),
    useCharged = cms.bool(False)
))

process.NewTauIDsEmbedded = cms.EDProducer("PATTauIDEmbedder",
    src = cms.InputTag("slimmedTaus"),
    tauIDSources = cms.PSet(
        byIsolationMVArun2v1DBoldDMwLTrawNew = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw"),
        byLooseIsolationMVArun2v1DBoldDMwLTNew = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1Loose"),
        byMediumIsolationMVArun2v1DBoldDMwLTNew = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1Medium"),
        byTightIsolationMVArun2v1DBoldDMwLTNew = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1Tight"),
        byVLooseIsolationMVArun2v1DBoldDMwLTNew = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1VLoose"),
        byVTightIsolationMVArun2v1DBoldDMwLTNew = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1VTight"),
        byVVLooseIsolationMVArun2v1DBoldDMwLTNew = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1VVLoose"),
        byVVTightIsolationMVArun2v1DBoldDMwLTNew = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1VVTight")
    )
)


process.NjettinessAK8 = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(999.0),
    akAxesR0 = cms.double(-999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(999),
    src = cms.InputTag("ak8CHSJets")
)


process.NjettinessAK8Puppi = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(999.0),
    akAxesR0 = cms.double(-999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(999),
    src = cms.InputTag("ak8PuppiJets")
)


process.ak4PFJetsCHS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("chs"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8CHSJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("chs"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8CHSJetsPruned = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nFilt = cms.int32(2),
    rParam = cms.double(0.8),
    rcut_factor = cms.double(0.5),
    src = cms.InputTag("chs"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    usePruning = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8CHSJetsSoftDrop = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("chs"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("packedGenParticles"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8GenJetsPruned = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nFilt = cms.int32(2),
    rParam = cms.double(0.8),
    rcut_factor = cms.double(0.5),
    src = cms.InputTag("packedGenParticles"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    usePruning = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8GenJetsSoftDrop = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("packedGenParticles"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8PFJetsPuppiPrunedMass = cms.EDProducer("RecoJetDeltaRValueMapProducer",
    distMax = cms.double(0.8),
    matched = cms.InputTag("ak8PuppiJetsPruned"),
    src = cms.InputTag("ak8PuppiJets"),
    value = cms.string('mass')
)


process.ak8PFJetsPuppiPrunedMassCorrected = cms.EDProducer("RecoJetDeltaRValueMapProducer",
    distMax = cms.double(0.8),
    matched = cms.InputTag("patJetsAk8PuppiJetsPrunedPacked"),
    src = cms.InputTag("ak8PuppiJets"),
    value = cms.string('mass')
)


process.ak8PFJetsPuppiSoftDropMass = cms.EDProducer("RecoJetDeltaRValueMapProducer",
    distMax = cms.double(0.8),
    matched = cms.InputTag("ak8PuppiJetsSoftDrop"),
    src = cms.InputTag("ak8PuppiJets"),
    value = cms.string('mass')
)


process.ak8PFJetsPuppiSoftDropMassCorrected = cms.EDProducer("RecoJetDeltaRValueMapProducer",
    distMax = cms.double(0.8),
    matched = cms.InputTag("patJetsAk8PuppiJetsSoftDropPacked"),
    src = cms.InputTag("ak8PuppiJets"),
    value = cms.string('mass')
)


process.ak8PuppiJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PuppiJetsPruned = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nFilt = cms.int32(2),
    rParam = cms.double(0.8),
    rcut_factor = cms.double(0.5),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    usePruning = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8PuppiJetsSoftDrop = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('MinPtCut'),
                isIgnored = cms.bool(False),
                minPt = cms.double(5.0),
                needsAdditionalProducts = cms.bool(False)
            ), 
                cms.PSet(
                    allowedEtaRanges = cms.VPSet(cms.PSet(
                        maxEta = cms.double(1.479),
                        minEta = cms.double(0.0)
                    ), 
                        cms.PSet(
                            maxEta = cms.double(2.5),
                            minEta = cms.double(1.479)
                        )),
                    cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    useAbsEta = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDEtaInSeedCut'),
                    dEtaInSeedCutValueEB = cms.double(0.00387),
                    dEtaInSeedCutValueEE = cms.double(0.0072),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDPhiInCut'),
                    dPhiInCutValueEB = cms.double(0.0716),
                    dPhiInCutValueEE = cms.double(0.147),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                    full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                    full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0356),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelC0 = cms.double(0.05),
                    barrelCE = cms.double(1.12),
                    barrelCr = cms.double(0.0368),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                    endcapC0 = cms.double(0.0414),
                    endcapCE = cms.double(0.5),
                    endcapCr = cms.double(0.201),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll")
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                    eInverseMinusPInverseCutValueEB = cms.double(0.129),
                    eInverseMinusPInverseCutValueEE = cms.double(0.0875),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                    isIgnored = cms.bool(False),
                    isRelativeIso = cms.bool(True),
                    isoCutEBHighPt = cms.double(0.133),
                    isoCutEBLowPt = cms.double(0.133),
                    isoCutEEHighPt = cms.double(0.146),
                    isoCutEELowPt = cms.double(0.146),
                    needsAdditionalProducts = cms.bool(True),
                    ptCutOff = cms.double(20.0),
                    rho = cms.InputTag("fixedGridRhoFastjetAll")
                ), 
                cms.PSet(
                    beamspotSrc = cms.InputTag("offlineBeamSpot"),
                    conversionSrc = cms.InputTag("allConversions"),
                    conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                    cutName = cms.string('GsfEleConversionVetoCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleMissingHitsCut'),
                    isIgnored = cms.bool(False),
                    maxMissingHitsEB = cms.uint32(1),
                    maxMissingHitsEE = cms.uint32(1),
                    needsAdditionalProducts = cms.bool(False)
                )),
            idName = cms.string('cutBasedElectronID-Fall17-94X-V1-loose'),
            isPOGApproved = cms.untracked.bool(True)
        ),
        idMD5 = cms.string('0b8456d622494441fe713a6858e0f7c1'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00365),
                        dEtaInSeedCutValueEE = cms.double(0.00625),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0588),
                        dPhiInCutValueEE = cms.double(0.0355),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0309),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0327),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0335),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0718),
                        isoCutEBLowPt = cms.double(0.0718),
                        isoCutEEHighPt = cms.double(0.143),
                        isoCutEELowPt = cms.double(0.143),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('a238ee70910de53d36866e89768500e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00353),
                        dEtaInSeedCutValueEE = cms.double(0.00567),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0499),
                        dPhiInCutValueEE = cms.double(0.0165),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0305),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0278),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0158),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0361),
                        isoCutEBLowPt = cms.double(0.0361),
                        isoCutEEHighPt = cms.double(0.094),
                        isoCutEELowPt = cms.double(0.094),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4acb2d2796efde7fba75380ce8823fc2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00523),
                        dEtaInSeedCutValueEE = cms.double(0.00984),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.159),
                        dPhiInCutValueEE = cms.double(0.157),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0128),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0445),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0962),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.168),
                        isoCutEBLowPt = cms.double(0.168),
                        isoCutEEHighPt = cms.double(0.185),
                        isoCutEELowPt = cms.double(0.185),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('43be9b381a8d9b0910b7f81a5ad8ff3a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.031),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(1e+30),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.02),
                        dPhiInCutValueEE = cms.double(1e+30),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.06),
                        hadronicOverEMCutValueEE = cms.double(0.065),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.013),
                        eInverseMinusPInverseCutValueEE = cms.double(0.013),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleCalPFClusterIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_HLT_ecalPFClusterIso.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.16),
                        isoCutEBLowPt = cms.double(0.16),
                        isoCutEEHighPt = cms.double(0.12),
                        isoCutEELowPt = cms.double(0.12),
                        isoType = cms.int32(0),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetCentralCalo")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleCalPFClusterIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_HLT_hcalPFClusterIso.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.12),
                        isoCutEBLowPt = cms.double(0.12),
                        isoCutEEHighPt = cms.double(0.12),
                        isoCutEELowPt = cms.double(0.12),
                        isoType = cms.int32(1),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetCentralCalo")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.0),
                        constTermEE = cms.double(0.0),
                        cutName = cms.string('GsfEleTrkPtIsoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.08),
                        slopeTermEE = cms.double(0.08)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleNormalizedGsfChi2Cut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        normalizedGsfChi2CutValueEB = cms.double(1e+30),
                        normalizedGsfChi2CutValueEE = cms.double(3.0)
                    )),
                idName = cms.string('cutBasedElectronHLTPreselection-Summer16-V1'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('aef5f00cc25a63b44192c6fc449f7dc0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(35.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.4442),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.566)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(0.006),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.06),
                        dPhiInCutValueEE = cms.double(0.06),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaWithSatCut'),
                        isIgnored = cms.bool(False),
                        maxNrSatCrysIn5x5EB = cms.int32(0),
                        maxNrSatCrysIn5x5EE = cms.int32(0),
                        maxSigmaIEtaIEtaEB = cms.double(9999),
                        maxSigmaIEtaIEtaEE = cms.double(0.03),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('GsfEleFull5x5E2x5OverE5x5WithSatCut'),
                        isIgnored = cms.bool(False),
                        maxNrSatCrysIn5x5EB = cms.int32(0),
                        maxNrSatCrysIn5x5EE = cms.int32(0),
                        minE1x5OverE5x5EB = cms.double(0.83),
                        minE1x5OverE5x5EE = cms.double(-1.0),
                        minE2x5OverE5x5EB = cms.double(0.94),
                        minE2x5OverE5x5EE = cms.double(-1.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.0),
                        constTermEE = cms.double(5),
                        cutName = cms.string('GsfEleHadronicOverEMLinearCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.05),
                        slopeTermEE = cms.double(0.05)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(5.0),
                        constTermEE = cms.double(5.0),
                        cutName = cms.string('GsfEleValueMapIsoRhoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag(""),
                        rhoEAEB = cms.double(0.0),
                        rhoEAEE = cms.double(0.0),
                        rhoEtStartEB = cms.double(999999.0),
                        rhoEtStartEE = cms.double(999999.0),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.0),
                        slopeTermEE = cms.double(0.0),
                        value = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.0),
                        constTermEE = cms.double(2.5),
                        cutName = cms.string('GsfEleEmHadD1IsoRhoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        rhoConstant = cms.double(0.28),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(50.0),
                        slopeTermEB = cms.double(0.03),
                        slopeTermEE = cms.double(0.03)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.02),
                        dxyCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEcalDrivenCut'),
                        ecalDrivenEB = cms.int32(1),
                        ecalDrivenEE = cms.int32(1),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('heepElectronID-HEEPV70'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('49b6b60e9f16727f241eb34b9d345a8f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring('0.9530240956555949 - exp(-pt / 2.7591425841003647) *  0.4669644718545271', 
                        '0.9336564763961019 - exp(-pt /  2.709276284272272) * 0.33512286599215946', 
                        '0.9313133688365339 - exp(-pt / 1.5821934800715558) *  3.8889462619659265', 
                        '0.9825268564943458 - exp(-pt /  8.702601455860762) *  1.1974861596609097', 
                        '0.9727509457929913 - exp(-pt /  8.179525631018565) *  1.7111755094657688', 
                        '0.9562619539540145 - exp(-pt /  8.109845366281608) *   3.013927699126942'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring('0.9165112826974601 - exp(-pt / 2.7381703555094217) *    1.03549199648109', 
                        '0.8655738322220173 - exp(-pt / 2.4027944652597073) *  0.7975615613282494', 
                        '-3016.035055227131 - exp(-pt / -52140.61856333602) * -3016.3029387236506', 
                        '0.9616542816132922 - exp(-pt /  8.757943837889817) *  3.1390200321591206', 
                        '0.9319258011430132 - exp(-pt /  8.846057432565809) *  3.5985063793347787', 
                        '0.8899260780999244 - exp(-pt / 10.124234115859881) *   4.352791250718547'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring('-0.13285867293779202', 
                        '-0.31765300958836074', 
                        '-0.0799205914718861', 
                        '-0.856871961305474', 
                        '-0.8107642141584835', 
                        '-0.7179265933023059'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("slimmedElectrons")
)


process.egmPhotonIDs = cms.EDProducer("VersionedPhotonIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('PhoMVACut'),
                isIgnored = cms.bool(False),
                mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                mvaCuts = cms.vdouble(0.42, 0.14),
                mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                needsAdditionalProducts = cms.bool(True)
            )),
            idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
            isPOGApproved = cms.bool(True)
        ),
        idMD5 = cms.string('3013ddce7a3ad8b54827c29f5d92282e'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(-0.02, -0.26),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('5c06832759b1faf7dd6fc45ed1aef3a2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.04596),
                        hadronicOverEMCutValueEE = cms.double(0.059),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0106),
                        cutValueEE = cms.double(0.0272),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.694),
                        C1_EE = cms.double(2.089),
                        C2_EB = cms.double(0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(24.032),
                        C1_EE = cms.double(19.722),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.876),
                        C1_EE = cms.double(4.162),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4578dfcceb0bfd1ba5ac28973c843fd0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02197),
                        hadronicOverEMCutValueEE = cms.double(0.0326),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01015),
                        cutValueEE = cms.double(0.0272),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.141),
                        C1_EE = cms.double(1.051),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.189),
                        C1_EE = cms.double(2.718),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.08),
                        C1_EE = cms.double(3.867),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('28b186c301061395f394a81266c8d7de'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02148),
                        hadronicOverEMCutValueEE = cms.double(0.0321),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00996),
                        cutValueEE = cms.double(0.0271),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.65),
                        C1_EE = cms.double(0.517),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.317),
                        C1_EE = cms.double(2.716),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.044),
                        C1_EE = cms.double(3.032),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('6f4f0ed6a8bf2de8dcf0bc3349b0546d'),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("slimmedPhotons")
)


process.egmPhotonIsolation = cms.EDProducer("CITKPFIsolationSumProducer",
    isolationConeDefinitions = cms.VPSet(cms.PSet(
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('h+'),
        isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
        miniAODVertexCodes = cms.vuint32(2, 3),
        particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
        vertexIndex = cms.int32(0)
    ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('h0'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('gamma'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        )),
    srcForIsolationCone = cms.InputTag("packedPFCandidates"),
    srcToIsolate = cms.InputTag("slimmedPhotons")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Phys14NonTrig25nsV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2VariablesClassic.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
    ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring15NonTrig25nsV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring15Trig50nsV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring15Trig25nsV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16HZZV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16GeneralPurposeV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz')
        )),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.electronMVAVariableHelper = cms.EDProducer("GsfElectronMVAVariableHelper",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    beamSpotMiniAOD = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices"),
    vertexCollectionMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.electronRegressionValueMapProducer = cms.EDProducer("ElectronRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.heepIDVarValueMaps = cms.EDProducer("ElectronHEEPIDValueMapProducer",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    candVetosAOD = cms.vstring('ELES', 
        'NONE', 
        'NONELES'),
    candVetosMiniAOD = cms.vstring('ELES', 
        'NONE', 
        'NONELES'),
    candsAOD = cms.VInputTag("packedCandsForTkIso", "lostTracksForTkIso", "lostTracksForTkIso:eleTracks"),
    candsMiniAOD = cms.VInputTag("packedPFCandidates", "lostTracks", "lostTracks:eleTracks"),
    dataFormat = cms.int32(0),
    ebRecHitsAOD = cms.InputTag("reducedEcalRecHitsEB"),
    ebRecHitsMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeRecHitsAOD = cms.InputTag("reducedEcalRecHitsEB"),
    eeRecHitsMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    elesAOD = cms.InputTag("gedGsfElectrons"),
    elesMiniAOD = cms.InputTag("slimmedElectrons"),
    trkIsoConfig = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    )
)


process.packedJetsAk8PuppiJets = cms.EDProducer("JetSubstructurePacker",
    algoLabels = cms.vstring('SoftDropPuppi'),
    algoTags = cms.VInputTag(cms.InputTag("patJetsAk8PuppiJetsSoftDropPacked")),
    distMax = cms.double(0.8),
    fixDaughters = cms.bool(False),
    jetSrc = cms.InputTag("patJetsAk8PuppiJets"),
    packedPFCandidates = cms.InputTag("packedPFCandidates")
)


process.patJetCorrFactorsAk8PuppiJets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8PuppiJetsPruned = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJetsPruned"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8PuppiJetsPrunedSubjets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJetsPruned","SubJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8PuppiJetsSoftDrop = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJetsSoftDrop"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetFlavourAssociationAk8PuppiJets = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJets"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAk8PuppiJetsPruned = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJetsPruned"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAk8PuppiJetsPrunedSubjets = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    groomedJets = cms.InputTag("ak8PuppiJetsPruned"),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJets"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8),
    subjets = cms.InputTag("ak8PuppiJetsPruned","SubJets")
)


process.patJetFlavourAssociationAk8PuppiJetsSoftDrop = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    groomedJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJets"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8),
    subjets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets")
)


process.patJetFlavourAssociationLegacyAk8PuppiJets = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8PuppiJets")
)


process.patJetFlavourAssociationLegacyAk8PuppiJetsPruned = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8PuppiJetsPruned")
)


process.patJetFlavourAssociationLegacyAk8PuppiJetsPrunedSubjets = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8PuppiJetsPrunedSubjets")
)


process.patJetFlavourAssociationLegacyAk8PuppiJetsSoftDrop = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8PuppiJetsSoftDrop")
)


process.patJetFlavourAssociationLegacyAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8PuppiJetsSoftDropSubjets")
)


process.patJetGenJetMatchAk8PuppiJets = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak8GenJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJets")
)


process.patJetGenJetMatchAk8PuppiJetsPruned = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsPruned")
)


process.patJetGenJetMatchAk8PuppiJetsPrunedSubjets = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak8GenJetsPruned","SubJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsPruned","SubJets")
)


process.patJetGenJetMatchAk8PuppiJetsSoftDrop = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsSoftDrop")
)


process.patJetGenJetMatchAk8PuppiJetsSoftDropSubjets = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak8GenJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets")
)


process.patJetPartonAssociationLegacyAk8PuppiJets = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJets"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8PuppiJetsPruned = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJetsPruned"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8PuppiJetsPrunedSubjets = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJetsPruned","SubJets"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8PuppiJetsSoftDrop = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonMatchAk8PuppiJets = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJets")
)


process.patJetPartonMatchAk8PuppiJetsPruned = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsPruned")
)


process.patJetPartonMatchAk8PuppiJetsPrunedSubjets = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsPruned","SubJets")
)


process.patJetPartonMatchAk8PuppiJetsSoftDrop = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsSoftDrop")
)


process.patJetPartonMatchAk8PuppiJetsSoftDropSubjets = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets")
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    fullChainPhysPartons = cms.bool(True),
    particles = cms.InputTag("prunedGenParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
    src = cms.InputTag("prunedGenParticles"),
    withLeptons = cms.bool(False)
)


process.patJetsAk8PuppiJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8PuppiJets"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8PuppiJets"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJets"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probbb"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJets"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probc"), 
        cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probb"), cms.InputTag("pfDeepCSVDiscriminatorsJetTagsAk8PuppiJets","BvsAll")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8PuppiJets"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8PuppiJets"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8PuppiJets")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJets"), cms.InputTag("pfDeepCSVTagInfosAk8PuppiJets"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJets"), cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJets"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJets")),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("", "ak8PFJetsPuppiSoftDropMass", "ak8PFJetsPuppiSoftDropMassCorrected", "NjettinessAK8Puppi:tau1", "NjettinessAK8Puppi:tau2", 
                "NjettinessAK8Puppi:tau3")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8PuppiJetsPruned = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8PuppiJetsPruned"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8PuppiJetsPruned"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsPruned"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probbb"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsPruned"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probc"), 
        cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probb"), cms.InputTag("pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsPruned","BvsAll")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8PuppiJetsPruned"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8PuppiJetsPruned"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8PuppiJetsPruned")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJetsPruned"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsPruned"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPruned"), cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsPruned"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsPruned"), cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsPruned"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsPruned")),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8PuppiJetsPrunedPacked = cms.EDProducer("BoostedJetMerger",
    jetSrc = cms.InputTag("patJetsAk8PuppiJetsPruned"),
    subjetSrc = cms.InputTag("patJetsAk8PuppiJetsPrunedSubjets")
)


process.patJetsAk8PuppiJetsPrunedSubjets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8PuppiJetsPrunedSubjets","SubJets"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8PuppiJetsPrunedSubjets"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsPrunedSubjets"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probbb"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsPrunedSubjets"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probc"), 
        cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probb"), cms.InputTag("pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsPrunedSubjets","BvsAll")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8PuppiJetsPrunedSubjets"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8PuppiJetsPrunedSubjets"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8PuppiJetsPrunedSubjets")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJetsPruned","SubJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsPrunedSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPrunedSubjets"), cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsPrunedSubjets"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsPrunedSubjets"), cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsPrunedSubjets"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsPrunedSubjets")),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8PuppiJetsSoftDrop = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8PuppiJetsSoftDrop"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8PuppiJetsSoftDrop"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsSoftDrop"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probbb"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDrop"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probc"), 
        cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probb"), cms.InputTag("pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsSoftDrop","BvsAll")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8PuppiJetsSoftDrop"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8PuppiJetsSoftDrop"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8PuppiJetsSoftDrop")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJetsSoftDrop"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDrop"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDrop")),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8PuppiJetsSoftDropPacked = cms.EDProducer("BoostedJetMerger",
    jetSrc = cms.InputTag("patJetsAk8PuppiJetsSoftDrop"),
    subjetSrc = cms.InputTag("patJetsAk8PuppiJetsSoftDropSubjets")
)


process.patJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8PuppiJetsSoftDropSubjets","SubJets"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8PuppiJetsSoftDropSubjets"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probbb"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probc"), 
        cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probb"), cms.InputTag("pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsSoftDropSubjets","BvsAll")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8PuppiJetsSoftDropSubjets"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8PuppiJetsSoftDropSubjets"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8PuppiJetsSoftDropSubjets")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDropSubjets"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDropSubjets")),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJets = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsPruned = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsPruned"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsPrunedSubjets = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsPrunedSubjets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDrop"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDropSubjets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJets"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsPruned = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsPruned"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsPrunedSubjets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsPrunedSubjets"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDrop = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDrop"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDropSubjets"))
)


process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJets"))
)


process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsPruned = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsPruned"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPruned"))
)


process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsPrunedSubjets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsPrunedSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPrunedSubjets"))
)


process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsSoftDrop = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop"))
)


process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets"))
)


process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJets = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(cms.PSet(
        denominator = cms.VInputTag(),
        name = cms.string('BvsAll'),
        numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probbb"))
    ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probc"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probbb")),
            name = cms.string('CvsB'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probc")),
            name = cms.string('CvsL'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJets","probc"))
        ))
)


process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsPruned = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(cms.PSet(
        denominator = cms.VInputTag(),
        name = cms.string('BvsAll'),
        numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probbb"))
    ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probc"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probbb")),
            name = cms.string('CvsB'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probc")),
            name = cms.string('CvsL'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPruned","probc"))
        ))
)


process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsPrunedSubjets = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(cms.PSet(
        denominator = cms.VInputTag(),
        name = cms.string('BvsAll'),
        numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probbb"))
    ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probc"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probbb")),
            name = cms.string('CvsB'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probc")),
            name = cms.string('CvsL'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets","probc"))
        ))
)


process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsSoftDrop = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(cms.PSet(
        denominator = cms.VInputTag(),
        name = cms.string('BvsAll'),
        numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probbb"))
    ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probc"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probbb")),
            name = cms.string('CvsB'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probc")),
            name = cms.string('CvsL'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probc"))
        ))
)


process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(cms.PSet(
        denominator = cms.VInputTag(),
        name = cms.string('BvsAll'),
        numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probbb"))
    ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probc"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probbb")),
            name = cms.string('CvsB'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probudsg"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probc")),
            name = cms.string('CvsL'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probc"))
        ))
)


process.pfDeepCSVJetTagsAk8PuppiJets = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourNoSL.json'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    src = cms.InputTag("pfDeepCSVTagInfosAk8PuppiJets"),
    toAdd = cms.PSet(
        probcc = cms.string('probc')
    )
)


process.pfDeepCSVJetTagsAk8PuppiJetsPruned = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourNoSL.json'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    src = cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsPruned"),
    toAdd = cms.PSet(
        probcc = cms.string('probc')
    )
)


process.pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourNoSL.json'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    src = cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsPrunedSubjets"),
    toAdd = cms.PSet(
        probcc = cms.string('probc')
    )
)


process.pfDeepCSVJetTagsAk8PuppiJetsSoftDrop = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourNoSL.json'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    src = cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsSoftDrop"),
    toAdd = cms.PSet(
        probcc = cms.string('probc')
    )
)


process.pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourNoSL.json'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    src = cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsSoftDropSubjets"),
    toAdd = cms.PSet(
        probcc = cms.string('probc')
    )
)


process.pfDeepCSVTagInfosAk8PuppiJets = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJets")
)


process.pfDeepCSVTagInfosAk8PuppiJetsPruned = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPruned")
)


process.pfDeepCSVTagInfosAk8PuppiJetsPrunedSubjets = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    fatJets = cms.InputTag("ak8PuppiJets"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsPruned"),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.8),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPrunedSubjets"),
    useSVClustering = cms.bool(True)
)


process.pfDeepCSVTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop")
)


process.pfDeepCSVTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    fatJets = cms.InputTag("ak8PuppiJets"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.8),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets"),
    useSVClustering = cms.bool(True)
)


process.pfImpactParameterAK8TagInfosAk8PuppiJets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJets"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8PuppiJetsPruned = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsPruned"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8PuppiJetsPrunedSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsPruned","SubJets"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8PuppiJets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8PuppiJetsPruned = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsPruned"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8PuppiJetsPrunedSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsPruned","SubJets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsPruned = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsPruned"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsPrunedSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    fatJets = cms.InputTag("ak8PuppiJets"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsPruned"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsPrunedSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    fatJets = cms.InputTag("ak8PuppiJets"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPruned = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsPruned"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPrunedSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    fatJets = cms.InputTag("ak8PuppiJets"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsPruned"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsPrunedSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    fatJets = cms.InputTag("ak8PuppiJets"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.photonMVAValueMapProducer = cms.EDProducer("PhotonMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring15NonTrig50nsV2p1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EE_V2.weights.xml.gz')
    ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('Run2Spring15NonTrig25nsV2p1'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EB_V2.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EE_V2.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('Run2Spring16NonTrigV1'),
            nCategories = cms.int32(2),
            phoIsoCutoff = cms.double(2.5),
            phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v1'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v1p1'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v2'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz')
        )),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.photonRegressionValueMapProducer = cms.EDProducer("PhotonRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.puppi = cms.EDProducer("PuppiProducer",
    DeltaZCut = cms.double(0.3),
    MinPuppiWeight = cms.double(0.01),
    PtMaxNeutrals = cms.double(200.0),
    UseDeltaZCut = cms.bool(True),
    algos = cms.VPSet(cms.PSet(
        EtaMaxExtrap = cms.double(2.0),
        MedEtaSF = cms.vdouble(1.0),
        MinNeutralPt = cms.vdouble(0.2),
        MinNeutralPtSlope = cms.vdouble(0.015),
        RMSEtaSF = cms.vdouble(1.0),
        etaMax = cms.vdouble(2.5),
        etaMin = cms.vdouble(0.0),
        ptMin = cms.vdouble(0.0),
        puppiAlgos = cms.VPSet(cms.PSet(
            algoId = cms.int32(5),
            applyLowPUCorr = cms.bool(True),
            combOpt = cms.int32(0),
            cone = cms.double(0.4),
            rmsPtMin = cms.double(0.1),
            rmsScaleFactor = cms.double(1.0),
            useCharged = cms.bool(True)
        ))
    ), 
        cms.PSet(
            EtaMaxExtrap = cms.double(2.0),
            MedEtaSF = cms.vdouble(0.9, 0.75),
            MinNeutralPt = cms.vdouble(1.7, 2.0),
            MinNeutralPtSlope = cms.vdouble(0.08, 0.08),
            RMSEtaSF = cms.vdouble(1.2, 0.95),
            etaMax = cms.vdouble(3.0, 10.0),
            etaMin = cms.vdouble(2.5, 3.0),
            ptMin = cms.vdouble(0.0, 0.0),
            puppiAlgos = cms.VPSet(cms.PSet(
                algoId = cms.int32(5),
                applyLowPUCorr = cms.bool(True),
                combOpt = cms.int32(0),
                cone = cms.double(0.4),
                rmsPtMin = cms.double(0.5),
                rmsScaleFactor = cms.double(1.0),
                useCharged = cms.bool(False)
            ))
        )),
    applyCHS = cms.bool(True),
    candName = cms.InputTag("packedPFCandidates"),
    clonePackedCands = cms.bool(False),
    invertPuppi = cms.bool(False),
    puppiDiagnostics = cms.bool(False),
    puppiForLeptons = cms.bool(False),
    useExistingWeights = cms.bool(False),
    useExp = cms.bool(False),
    useWeightsNoLep = cms.bool(False),
    vertexName = cms.InputTag("offlineSlimmedPrimaryVertices"),
    vtxNdofCut = cms.int32(4),
    vtxZCut = cms.double(24)
)


process.rerunDiscriminationByIsolationMVArun2v1Loose = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff80'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1Medium = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff70'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1Tight = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff60'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1VLoose = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff90'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1VTight = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff50'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1VVLoose = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff95'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1VVTight = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff40'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1raw = cms.EDProducer("PATTauDiscriminationByMVAIsolationRun2",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    loadMVAfromDB = cms.bool(True),
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    requireDecayMode = cms.bool(True),
    srcChargedIsoPtSum = cms.string('chargedIsoPtSum'),
    srcFootprintCorrection = cms.string('footprintCorrection'),
    srcNeutralIsoPtSum = cms.string('neutralIsoPtSum'),
    srcPUcorrPtSum = cms.string('puCorrPtSum'),
    srcPhotonPtSumOutsideSignalCone = cms.string('photonPtSumOutsideSignalCone'),
    verbosity = cms.int32(0)
)


process.chs = cms.EDFilter("CandPtrSelector",
    cut = cms.string('fromPV'),
    src = cms.InputTag("packedPFCandidates")
)


process.selectedPatJetsAk8PuppiJets = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("patJetsAk8PuppiJets")
)


process.selectedPatJetsAk8PuppiJetsPruned = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("patJetsAk8PuppiJetsPruned")
)


process.selectedPatJetsAk8PuppiJetsPrunedSubjets = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("patJetsAk8PuppiJetsPrunedSubjets")
)


process.selectedPatJetsAk8PuppiJetsSoftDrop = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("patJetsAk8PuppiJetsSoftDrop")
)


process.selectedPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("patJetsAk8PuppiJetsSoftDropSubjets")
)


process.ntuplizer = cms.EDAnalyzer("Ntuplizer",
    HLT = cms.InputTag("TriggerResults","","HLT"),
    PUInfo = cms.InputTag("slimmedAddPileupInfo"),
    corrMetPx = cms.string('+0.1166 + 0.0200*Nvtx'),
    corrMetPy = cms.string('+0.2764 - 0.1280*Nvtx'),
    doAK4Jets = cms.bool(True),
    doAK8Jets = cms.bool(True),
    doBoostedTaus = cms.bool(False),
    doElectrons = cms.bool(False),
    doGenEvent = cms.bool(False),
    doGenJets = cms.bool(False),
    doGenParticles = cms.bool(False),
    doHbbTag = cms.bool(False),
    doHltFilters = cms.bool(False),
    doMETSVFIT = cms.bool(False),
    doMVAMET = cms.bool(False),
    doMissingEt = cms.bool(False),
    doMultipleTauMVAversions = cms.bool(False),
    doMuons = cms.bool(False),
    doPhotons = cms.bool(True),
    doPileUp = cms.bool(False),
    doPrunedSubjets = cms.bool(False),
    doPuppi = cms.bool(True),
    doTaus = cms.bool(False),
    doTriggerDecisions = cms.bool(True),
    doTriggerObjects = cms.bool(False),
    doTrimming = cms.bool(False),
    doVertices = cms.bool(True),
    dupCluster = cms.InputTag("particleFlowEGammaGSFixed","dupECALClusters"),
    ebRecHits = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eleHEEPIdMap = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70"),
    eleHLTIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronHLTPreselection-Summer16-V1"),
    eleLooseIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
    eleMVAMediumIdMap = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp90"),
    eleMVATightIdMap = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp80"),
    eleMediumIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
    eleTightIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
    eleVetoIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto"),
    electrons = cms.InputTag("slimmedElectrons"),
    externallheProducer = cms.InputTag("externalLHEProducer"),
    fatjets = cms.InputTag("slimmedJetsAK8"),
    genEventInfo = cms.InputTag("generator"),
    genJets = cms.InputTag("slimmedGenJets"),
    genJetsAK8 = cms.InputTag(""),
    genparticles = cms.InputTag("prunedGenParticles"),
    hitsNotReplaced = cms.InputTag("ecalMultiAndGSGlobalRecHitEB","hitsNotReplaced"),
    jecAK4chsPayloadNames = cms.vstring('JEC/Fall17_17Nov2017C_V32_DATA_L1FastJet_AK4PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L2Relative_AK4PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L3Absolute_AK4PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L2L3Residual_AK4PFPuppi.txt'),
    jecAK4chsUnc = cms.string('JEC/Fall17_17Nov2017C_V32_DATA_Uncertainty_AK4PFPuppi.txt'),
    jecAK4forMetCorr = cms.vstring(),
    jecAK8GroomedchsPayloadNames = cms.vstring('JEC/Fall17_17Nov2017C_V32_DATA_L2Relative_AK8PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L3Absolute_AK8PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L2L3Residual_AK8PFPuppi.txt'),
    jecAK8PuppiPayloadNames = cms.vstring('JEC/Fall17_17Nov2017C_V32_DATA_L2Relative_AK8PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L3Absolute_AK8PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L2L3Residual_AK8PFPuppi.txt'),
    jecAK8chsPayloadNames = cms.vstring('JEC/Fall17_17Nov2017C_V32_DATA_L1FastJet_AK8PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L2Relative_AK8PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L3Absolute_AK8PFPuppi.txt', 
        'JEC/Fall17_17Nov2017C_V32_DATA_L2L3Residual_AK8PFPuppi.txt'),
    jecAK8chsUnc = cms.string('JEC/Fall17_17Nov2017C_V32_DATA_Uncertainty_AK8PFPuppi.txt'),
    jecpath = cms.string(''),
    jerAK4Puppi_res_PayloadNames = cms.string('JER/Spring16_25nsV6_MC_PtResolution_AK4PFPuppi.txt'),
    jerAK4Puppi_sf_PayloadNames = cms.string('JER/Spring16_25nsV6_MC_SF_AK4PFPuppi.txt'),
    jerAK4chs_res_PayloadNames = cms.string('JER/Spring16_25nsV6_MC_PtResolution_AK4PFchs.txt'),
    jerAK4chs_sf_PayloadNames = cms.string('JER/Spring16_25nsV6_MC_SF_AK4PFchs.txt'),
    jerAK8Puppi_res_PayloadNames = cms.string('JER/Spring16_25nsV6_MC_PtResolution_AK8PFPuppi.txt'),
    jerAK8Puppi_sf_PayloadNames = cms.string('JER/Spring16_25nsV6_MC_SF_AK8PFPuppi.txt'),
    jerAK8chs_res_PayloadNames = cms.string('JER/Spring16_25nsV6_MC_PtResolution_AK8PFchs.txt'),
    jerAK8chs_sf_PayloadNames = cms.string('JER/Spring16_25nsV6_MC_SF_AK8PFchs.txt'),
    jets = cms.InputTag("slimmedJets"),
    jetsForMetCorr = cms.InputTag("slimmedJets"),
    mets = cms.InputTag("slimmedMETs"),
    mets_EGclean = cms.InputTag("slimmedMETsEGClean"),
    mets_MEGclean = cms.InputTag("slimmedMETsMuEGClean"),
    mets_mva = cms.InputTag("MVAMET","MVAMET"),
    mets_puppi = cms.InputTag("slimmedMETsPuppi"),
    mets_uncorr = cms.InputTag("slimmedMETsUncorrected"),
    muons = cms.InputTag("slimmedMuons"),
    mvaCategoriesMap = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
    mvaValuesMap = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
    noiseFilter = cms.InputTag("TriggerResults","","RECO"),
    noiseFilterSelection_CSCTightHalo2015Filter = cms.string('Flag_CSCTightHalo2015Filter'),
    noiseFilterSelection_CSCTightHaloFilter = cms.string('Flag_CSCTightHaloFilter'),
    noiseFilterSelection_CSCTightHaloTrkMuUnvetoFilter = cms.string('Flag_CSCTightHaloTrkMuUnvetoFilter'),
    noiseFilterSelection_EcalDeadCellTriggerPrimitiveFilter = cms.string('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    noiseFilterSelection_HBHENoiseFilter = cms.string('Flag_HBHENoiseFilter'),
    noiseFilterSelection_HBHENoiseFilterLoose = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Loose"),
    noiseFilterSelection_HBHENoiseFilterTight = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Tight"),
    noiseFilterSelection_HBHENoiseIsoFilter = cms.InputTag("HBHENoiseFilterResultProducer","HBHEIsoNoiseFilterResult"),
    noiseFilterSelection_HcalStripHaloFilter = cms.string('Flag_HcalStripHaloFilter'),
    noiseFilterSelection_badMuonsFilter = cms.string('Flag_badMuons'),
    noiseFilterSelection_chargedHadronTrackResolutionFilter = cms.string('Flag_chargedHadronTrackResolutionFilter'),
    noiseFilterSelection_duplicateMuonsFilter = cms.string('Flag_duplicateMuons'),
    noiseFilterSelection_ecalLaserCorrFilter = cms.string('Flag_ecalLaserCorrFilter'),
    noiseFilterSelection_eeBadScFilter = cms.string('Flag_eeBadScFilter'),
    noiseFilterSelection_globalSuperTightHalo2016Filter = cms.string('Flag_globalSuperTightHalo2016Filter'),
    noiseFilterSelection_globalTightHalo2016Filter = cms.string('Flag_globalTightHalo2016Filter'),
    noiseFilterSelection_goodVertices = cms.string('Flag_goodVertices'),
    noiseFilterSelection_hcalLaserEventFilter = cms.string('Flag_hcalLaserEventFilter'),
    noiseFilterSelection_metFilters = cms.string('Flag_METFilters'),
    noiseFilterSelection_muonBadTrackFilter = cms.string('Flag_muonBadTrackFilter'),
    noiseFilterSelection_nobadMuonsFilter = cms.string('Flag_nobadMuons'),
    noiseFilterSelection_trackingFailureFilter = cms.string('Flag_trackingFailureFilter'),
    noiseFilterSelection_trkPOGFilters = cms.string('Flag_trkPOGFilters'),
    noiseFilterSelection_trkPOG_logErrorTooManyClusters = cms.string('Flag_trkPOG_logErrorTooManyClusters'),
    noiseFilterSelection_trkPOG_manystripclus53X = cms.string('Flag_trkPOG_manystripclus53X'),
    noiseFilterSelection_trkPOG_toomanystripclus53X = cms.string('Flag_trkPOG_toomanystripclus53X'),
    packedpfcandidates = cms.InputTag("packedPFCandidates"),
    phoIdVerbose = cms.bool(False),
    phoLooseIdMap = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose"),
    phoMediumIdMap = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium"),
    phoMvaCategoriesMap = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
    phoMvaValuesMap = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
    phoTightIdMap = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight"),
    photons = cms.InputTag("slimmedPhotons"),
    prunedjets = cms.InputTag(""),
    puppijets = cms.InputTag("slimmedJetsAK8"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runOnMC = cms.bool(False),
    softdropjets = cms.InputTag(""),
    subjetflavour = cms.InputTag("AK8byValAlgo"),
    taus = cms.InputTag("NewTauIDsEmbedded"),
    tausBoostedTau = cms.InputTag("slimmedTaus"),
    triggerobjects = cms.InputTag("slimmedPatTrigger"),
    triggerprescales = cms.InputTag("patTrigger"),
    trimmedjets = cms.InputTag(""),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary', 
        'Ntuple'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(1)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('flatTuple.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.candidateBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_v4.weights.xml.gz')
)


process.candidateBoostedDoubleSecondaryVertexCA15Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_CA15_BDT_v3.weights.xml.gz')
)


process.candidateChargeBTagComputer = cms.ESProducer("CandidateChargeBTagESProducer",
    gbrForestLabel = cms.string(''),
    jetChargeExp = cms.double(0.8),
    svChargeExp = cms.double(0.5),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/ChargeBTag_4sep_2016.weights.xml.gz')
)


process.candidateCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring('candidateJetProbabilityComputer', 
        'candidateJetBProbabilityComputer', 
        'candidateCombinedSecondaryVertexV2Computer', 
        'softPFMuonComputer', 
        'softPFElectronComputer'),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring('Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidateCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexSoftLeptonCvsLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCvsLESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLeptonCvsL', 
        'CombinedSVPseudoVertexNoSoftLeptonCvsL', 
        'CombinedSVNoVertexNoSoftLeptonCvsL', 
        'CombinedSVRecoVertexSoftMuonCvsL', 
        'CombinedSVPseudoVertexSoftMuonCvsL', 
        'CombinedSVNoVertexSoftMuonCvsL', 
        'CombinedSVRecoVertexSoftElectronCvsL', 
        'CombinedSVPseudoVertexSoftElectronCvsL', 
        'CombinedSVNoVertexSoftElectronCvsL'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateGhostTrackComputer = cms.ESProducer("CandidateGhostTrackESProducer",
    calibrationRecords = cms.vstring('GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    recordLabel = cms.string(''),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True)
)


process.candidateJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring('candidateNegativeOnlyJetProbabilityComputer', 
        'candidateNegativeOnlyJetBProbabilityComputer', 
        'candidateNegativeCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring('Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidateNegativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D2ndComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D3rdComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring('candidatePositiveOnlyJetProbabilityComputer', 
        'candidatePositiveOnlyJetBProbabilityComputer', 
        'candidatePositiveCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring('Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidatePositiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateSimpleSecondaryVertex2TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateSimpleSecondaryVertex3TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateTrackCounting3D2ndComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateTrackCounting3D3rdComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.charmTagsComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_sklearn.weight.xml')
)


process.charmTagsComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_sklearn.weight.xml')
)


process.charmTagsNegativeComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(True),
        calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(True),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(-2.0),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(True)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_sklearn.weight.xml')
)


process.charmTagsNegativeComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(True),
        calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(True),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(-2.0),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(True)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_sklearn.weight.xml')
)


process.charmTagsPositiveComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_sklearn.weight.xml')
)


process.charmTagsPositiveComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_sklearn.weight.xml')
)


process.combinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring('jetProbabilityComputer', 
        'jetBProbabilityComputer', 
        'combinedSecondaryVertexV2Computer', 
        'softPFMuonComputer', 
        'softPFElectronComputer'),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring('Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.combinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.doubleVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    minVertices = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.ghostTrackComputer = cms.ESProducer("GhostTrackESProducer",
    calibrationRecords = cms.vstring('GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    recordLabel = cms.string(''),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True)
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.impactParameterMVAComputer = cms.ESProducer("GenericMVAJetTagESProducer",
    calibrationRecord = cms.string('ImpactParameterMVA'),
    recordLabel = cms.string(''),
    useCategories = cms.bool(False)
)


process.jetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.jetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring('negativeOnlyJetProbabilityComputer', 
        'negativeOnlyJetBProbabilityComputer', 
        'negativeCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring('Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.negativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.negativeOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.negativeSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.negativeTrackCounting3D2ndComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.negativeTrackCounting3D3rdComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.positiveCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring('positiveOnlyJetProbabilityComputer', 
        'positiveOnlyJetBProbabilityComputer', 
        'positiveCombinedSecondaryVertexV2Computer', 
        'positiveSoftPFMuonComputer', 
        'positiveSoftPFElectronComputer'),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring('Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.positiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.positiveOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.positiveSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.simpleSecondaryVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.simpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.softPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.softPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackCounting3D2ndComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackCounting3D3rdComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.BTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('94X_dataRun2_v6'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497),
        HFdepthOneParameterB = cms.vdouble(-4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209),
        HFdepthTwoParameterA = cms.vdouble(0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593),
        HFdepthTwoParameterB = cms.vdouble(-2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06)
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(cms.PSet(
        crosstalk = cms.double(0.0),
        nonlin1 = cms.double(1.0),
        nonlin2 = cms.double(0.0),
        nonlin3 = cms.double(0.0),
        pixels = cms.int32(36000)
    ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.000439367311072),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(203),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(44.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.69e-11, 7.9e-11),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(203)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.000439367311072),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(203),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(44.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.69e-11, 7.9e-11),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(203)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.loadRecoTauTagMVAsFromPrepDB = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string(''),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet( (cms.PSet(
        label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1'),
        record = cms.string('GBRWrapperRcd'),
        tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1')
    ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff95')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff95')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff95')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff95')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff99_5'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff99_5')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff99_0'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff99_0')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff98_0'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff98_0')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff95')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization')
        ) ) )
)


process.prefer("es_hardcode")

process.egmPhotonIsolationMiniAODTask = cms.Task(process.egmPhotonIsolation)


process.egmGsfElectronIDTask = cms.Task(process.egmGsfElectronIDs, process.electronMVAValueMapProducer, process.electronMVAVariableHelper, process.electronRegressionValueMapProducer)


process.patAlgosToolsTask = cms.Task(process.egmGsfElectronIDTask, process.heepIDVarValueMaps, process.patJetCorrFactorsAk8PuppiJets, process.patJetCorrFactorsAk8PuppiJetsPruned, process.patJetCorrFactorsAk8PuppiJetsPrunedSubjets, process.patJetCorrFactorsAk8PuppiJetsSoftDrop, process.patJetCorrFactorsAk8PuppiJetsSoftDropSubjets, process.patJetFlavourAssociationAk8PuppiJets, process.patJetFlavourAssociationAk8PuppiJetsPruned, process.patJetFlavourAssociationAk8PuppiJetsPrunedSubjets, process.patJetFlavourAssociationAk8PuppiJetsSoftDrop, process.patJetFlavourAssociationAk8PuppiJetsSoftDropSubjets, process.patJetFlavourAssociationLegacyAk8PuppiJets, process.patJetFlavourAssociationLegacyAk8PuppiJetsPruned, process.patJetFlavourAssociationLegacyAk8PuppiJetsPrunedSubjets, process.patJetFlavourAssociationLegacyAk8PuppiJetsSoftDrop, process.patJetFlavourAssociationLegacyAk8PuppiJetsSoftDropSubjets, process.patJetGenJetMatchAk8PuppiJets, process.patJetGenJetMatchAk8PuppiJetsPruned, process.patJetGenJetMatchAk8PuppiJetsPrunedSubjets, process.patJetGenJetMatchAk8PuppiJetsSoftDrop, process.patJetGenJetMatchAk8PuppiJetsSoftDropSubjets, process.patJetPartonAssociationLegacyAk8PuppiJets, process.patJetPartonAssociationLegacyAk8PuppiJetsPruned, process.patJetPartonAssociationLegacyAk8PuppiJetsPrunedSubjets, process.patJetPartonAssociationLegacyAk8PuppiJetsSoftDrop, process.patJetPartonAssociationLegacyAk8PuppiJetsSoftDropSubjets, process.patJetPartonMatchAk8PuppiJets, process.patJetPartonMatchAk8PuppiJetsPruned, process.patJetPartonMatchAk8PuppiJetsPrunedSubjets, process.patJetPartonMatchAk8PuppiJetsSoftDrop, process.patJetPartonMatchAk8PuppiJetsSoftDropSubjets, process.patJetPartons, process.patJetPartonsLegacy, process.patJetsAk8PuppiJets, process.patJetsAk8PuppiJetsPruned, process.patJetsAk8PuppiJetsPrunedSubjets, process.patJetsAk8PuppiJetsSoftDrop, process.patJetsAk8PuppiJetsSoftDropSubjets, process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJets, process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsPruned, process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsPrunedSubjets, process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDrop, process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDropSubjets, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJets, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsPruned, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsPrunedSubjets, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDrop, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDropSubjets, process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJets, process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsPruned, process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsPrunedSubjets, process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsSoftDrop, process.pfCombinedInclusiveSecondaryVertexV2BJetTagsAk8PuppiJetsSoftDropSubjets, process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJets, process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsPruned, process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsPrunedSubjets, process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsSoftDrop, process.pfDeepCSVDiscriminatorsJetTagsAk8PuppiJetsSoftDropSubjets, process.pfDeepCSVJetTagsAk8PuppiJets, process.pfDeepCSVJetTagsAk8PuppiJetsPruned, process.pfDeepCSVJetTagsAk8PuppiJetsPrunedSubjets, process.pfDeepCSVJetTagsAk8PuppiJetsSoftDrop, process.pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets, process.pfDeepCSVTagInfosAk8PuppiJets, process.pfDeepCSVTagInfosAk8PuppiJetsPruned, process.pfDeepCSVTagInfosAk8PuppiJetsPrunedSubjets, process.pfDeepCSVTagInfosAk8PuppiJetsSoftDrop, process.pfDeepCSVTagInfosAk8PuppiJetsSoftDropSubjets, process.pfImpactParameterAK8TagInfosAk8PuppiJets, process.pfImpactParameterAK8TagInfosAk8PuppiJetsPruned, process.pfImpactParameterAK8TagInfosAk8PuppiJetsPrunedSubjets, process.pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDrop, process.pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDropSubjets, process.pfImpactParameterTagInfosAk8PuppiJets, process.pfImpactParameterTagInfosAk8PuppiJetsPruned, process.pfImpactParameterTagInfosAk8PuppiJetsPrunedSubjets, process.pfImpactParameterTagInfosAk8PuppiJetsSoftDrop, process.pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJets, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsPruned, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsPrunedSubjets, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDrop, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJets, process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPruned, process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsPrunedSubjets, process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop, process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets, process.selectedPatJetsAk8PuppiJets, process.selectedPatJetsAk8PuppiJetsPruned, process.selectedPatJetsAk8PuppiJetsPrunedSubjets, process.selectedPatJetsAk8PuppiJetsSoftDrop, process.selectedPatJetsAk8PuppiJetsSoftDropSubjets)


process.egmPhotonIDTask = cms.Task(process.egmPhotonIDs, process.egmPhotonIsolationMiniAODTask, process.photonIDValueMapProducer, process.photonMVAValueMapProducer, process.photonRegressionValueMapProducer)


process.egmPhotonIDSequence = cms.Sequence(cms.Sequence(process.egmPhotonIDTask))


process.egmGsfElectronIDSequence = cms.Sequence(process.egmGsfElectronIDs, cms.Task(process.heepIDVarValueMaps))


process.egmPhotonIsolationMiniAODSequence = cms.Sequence(process.egmPhotonIsolationMiniAODTask)


process.rerunMvaIsolation2SeqRun2 = cms.Sequence(process.rerunDiscriminationByIsolationMVArun2v1raw+process.rerunDiscriminationByIsolationMVArun2v1VLoose+process.rerunDiscriminationByIsolationMVArun2v1VVLoose+process.rerunDiscriminationByIsolationMVArun2v1Loose+process.rerunDiscriminationByIsolationMVArun2v1Medium+process.rerunDiscriminationByIsolationMVArun2v1Tight+process.rerunDiscriminationByIsolationMVArun2v1VTight+process.rerunDiscriminationByIsolationMVArun2v1VVTight)


process.p = cms.Path(process.rerunMvaIsolation2SeqRun2+process.NewTauIDsEmbedded+process.egmPhotonIDSequence+process.ntuplizer, process.patAlgosToolsTask)


