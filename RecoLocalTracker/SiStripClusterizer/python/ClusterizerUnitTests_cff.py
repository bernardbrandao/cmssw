import FWCore.ParameterSet.Config as cms    

from RecoLocalTracker.SiStripClusterizer.ClusterizerUnitTestFunctions_cff import *

ClusterizerDefaultGroup = ClusterizerTest( "Default Clusterizer Settings",
                                           dict( channel=2, seed=3, cluster=5, hole=0, nBad=1, nAdj=0),
                                           [ DetUnit( "One digi",
                                                      [ digi(  10, 110,  noise1, gain1, good)  ],
                                                      [ cluster(  10, [110])
                                                        ] ),
                                             DetUnit( "Two digis",
                                                      [ digi(  10, 110,  noise1, gain1, good),
                                                        digi(  11, 100,  noise1, gain1, good) ],
                                                      [ cluster(  10, [110, 100])
                                                        ] ),
                                             DetUnit( "Two gains",
                                                      [ digi(  127, 110,  noise1, gain1, good),
                                                        digi(  128, 110,  noise1, 1.1, good) ],
                                                      [ cluster(  127, [110, 100])
                                                        ] ),
                                             DetUnit( "Three digis, middle is bad",
                                                      [ digi(  10, 110,  noise1, gain1, good),
                                                        digi(  11, 110,  noise1, gain1,  bad),
                                                        digi(  12, 100,  noise1, gain1, good) ],
                                                      [ cluster(  10, [110, 0, 100])
                                                        ] ),
                                             DetUnit( "Three digis, middle is bad and below channel",
                                                      [ digi(  10, 110,  noise1, gain1, good),
                                                        digi(  11,   0,  noise1, gain1,  bad),
                                                        digi(  12, 100,  noise1, gain1, good) ],
                                                      [ cluster(  10, [110, 0, 100])
                                                        ] ),
                                             DetUnit( "Three digis, middle is below channel",
                                                      [ digi(  10, 110,  noise1, gain1, good),
                                                        digi(  11,   0,  noise1, gain1, good),
                                                        digi(  12, 100,  noise1, gain1, good) ],
                                                      [ cluster(  10, [110]),
                                                        cluster(  12, [100])
                                                        ] ),
                                             DetUnit( "Wide cluster",
                                                      [ digi(  10, 110,  noise1, gain1, good),
                                                        digi(  11, 110,  noise1, gain1, good),
                                                        digi(  12, 110,  noise1, gain1, good),
                                                        digi(  13, 110,  noise1, gain1, good),
                                                        digi(  14, 110,  noise1, gain1, good),
                                                        digi(  15, 110,  noise1, gain1, good),
                                                        digi(  16, 110,  noise1, gain1, good),
                                                        digi(  17, 110,  noise1, gain1, good),
                                                        digi(  18, 110,  noise1, gain1, good),
                                                        digi(  19,  20,  noise1, gain1, good),
                                                        digi(  20, 100,  noise1, gain1, good) ],
                                                      [ cluster(  10, [110,110,110,110,110,110,110,110,110,20,100])
                                                        ] )
                                             ]
                                           )


