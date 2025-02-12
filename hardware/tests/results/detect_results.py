# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


GET_CPUS_RESULT = [('cpu', 'physical', 'number', 2),
                   ('cpu', 'physical_0', 'vendor', 'FakeAMD'),
                   ('cpu', 'physical_0', 'product',
                   'AMD: EPYC 7451 24-Core Processor'),
                   ('cpu', 'physical_0', 'cores', 24),
                   ('cpu', 'physical_0', 'threads', 48),
                   ('cpu', 'physical_0', 'family', 23),
                   ('cpu', 'physical_0', 'model', 1),
                   ('cpu', 'physical_0', 'stepping', 2),
                   ('cpu', 'physical_0', 'l1d cache', '32K'),
                   ('cpu', 'physical_0', 'l1i cache', '64K'),
                   ('cpu', 'physical_0', 'l2 cache', '512K'),
                   ('cpu', 'physical_0', 'l3 cache', '8192K'),
                   ('cpu', 'physical_0', 'min_Mhz', 1200.0),
                   ('cpu', 'physical_0', 'max_Mhz', 2300.0),
                   ('cpu', 'physical_0', 'current_Mhz', 1197.549),
                   ('cpu', 'physical_0', 'flags',
                   'fpu vme de pse tsc msr pae mce cx8 apic sep mtrr '
                    'pge mca cmov pat pse36 clflush mmx fxsr sse sse2 '
                    'ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp '
                    'lm constant_tsc rep_good nopl nonstop_tsc '
                    'cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq '
                    'monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes '
                    'xsave avx f16c rdrand lahf_lm cmp_legacy svm '
                    'extapic cr8_legacy abm sse4a misalignsse '
                    '3dnowprefetch osvw skinit wdt tce topoext '
                    'perfctr_core perfctr_nb bpext perfctr_llc '
                    'mwaitx cpb hw_pstate ssbd ibpb vmmcall '
                    'fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap '
                    'clflushopt sha_ni xsaveopt xsavec xgetbv1 '
                    'xsaves clzero irperf xsaveerptr arat npt lbrv '
                    'svm_lock nrip_save tsc_scale vmcb_clean '
                    'flushbyasid decodeassists pausefilter '
                    'pfthreshold avic v_vmsave_vmload vgif '
                    'overflow_recov succor smca'),
                   ('cpu', 'physical_1', 'vendor', 'FakeAMD'),
                   ('cpu', 'physical_1', 'product',
                   'AMD: EPYC 7451 24-Core Processor'),
                   ('cpu', 'physical_1', 'cores', 24),
                   ('cpu', 'physical_1', 'threads', 48),
                   ('cpu', 'physical_1', 'family', 23),
                   ('cpu', 'physical_1', 'model', 1),
                   ('cpu', 'physical_1', 'stepping', 2),
                   ('cpu', 'physical_1', 'l1d cache', '32K'),
                   ('cpu', 'physical_1', 'l1i cache', '64K'),
                   ('cpu', 'physical_1', 'l2 cache', '512K'),
                   ('cpu', 'physical_1', 'l3 cache', '8192K'),
                   ('cpu', 'physical_1', 'min_Mhz', 1200.0),
                   ('cpu', 'physical_1', 'max_Mhz', 2300.0),
                   ('cpu', 'physical_1', 'current_Mhz', 1197.549),
                   ('cpu', 'physical_1', 'flags',
                   'fpu vme de pse tsc msr pae mce cx8 apic sep mtrr '
                    'pge mca cmov pat pse36 clflush mmx fxsr sse sse2 '
                    'ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp '
                    'lm constant_tsc rep_good nopl nonstop_tsc '
                    'cpuid extd_apicid amd_dcm aperfmperf pni pclmulqdq '
                    'monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes '
                    'xsave avx f16c rdrand lahf_lm cmp_legacy svm '
                    'extapic cr8_legacy abm sse4a misalignsse '
                    '3dnowprefetch osvw skinit wdt tce topoext '
                    'perfctr_core perfctr_nb bpext perfctr_llc '
                    'mwaitx cpb hw_pstate ssbd ibpb vmmcall '
                    'fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap '
                    'clflushopt sha_ni xsaveopt xsavec xgetbv1 '
                    'xsaves clzero irperf xsaveerptr arat npt lbrv '
                    'svm_lock nrip_save tsc_scale vmcb_clean '
                    'flushbyasid decodeassists pausefilter '
                    'pfthreshold avic v_vmsave_vmload vgif '
                    'overflow_recov succor smca'),
                   ('cpu', 'logical', 'number', 1),
                   ('numa', 'nodes', 'count', 8),
                   ('numa', 'node_0', 'cpu_count', 12),
                   ('numa', 'node_0', 'cpu_mask', '0x3f00000000003f'),
                   ('numa', 'node_1', 'cpu_count', 12),
                   ('numa', 'node_1', 'cpu_mask', '0xfc0000000000fc0'),
                   ('numa', 'node_2', 'cpu_count', 12),
                   ('numa', 'node_2', 'cpu_mask', '0x3f00000000003f000'),
                   ('numa', 'node_3', 'cpu_count', 12),
                   ('numa', 'node_3', 'cpu_mask', '0xfc0000000000fc0000'),
                   ('numa', 'node_4', 'cpu_count', 12),
                   ('numa', 'node_4', 'cpu_mask', '0x3f00000000003f000000'),
                   ('numa', 'node_5', 'cpu_count', 12),
                   ('numa', 'node_5', 'cpu_mask', '0xfc0000000000fc0000000'),
                   ('numa', 'node_6', 'cpu_count', 12),
                   ('numa', 'node_6', 'cpu_mask', '0x3f00000000003f000000000'),
                   ('numa', 'node_7', 'cpu_count', 12),
                   ('numa', 'node_7', 'cpu_mask',
                    '0xfc0000000000fc0000000000')]


GET_CPUS_VM_RESULT = [('cpu', 'physical', 'number', 1),
                      ('cpu', 'physical_0', 'vendor', 'GenuineIntel'),
                      ('cpu', 'physical_0', 'product',
                      'Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz'),
                      ('cpu', 'physical_0', 'cores', 2),
                      ('cpu', 'physical_0', 'threads', 2),
                      ('cpu', 'physical_0', 'family', 6),
                      ('cpu', 'physical_0', 'model', 142),
                      ('cpu', 'physical_0', 'stepping', 10),
                      ('cpu', 'physical_0', 'l1d cache', '32K'),
                      ('cpu', 'physical_0', 'l1i cache', '32K'),
                      ('cpu', 'physical_0', 'l2 cache', '256K'),
                      ('cpu', 'physical_0', 'l3 cache', '8192K'),
                      ('cpu', 'physical_0', 'current_Mhz', 2112.002),
                      ('cpu', 'physical_0', 'flags',
                          'fpu vme de pse tsc msr pae mce cx8 apic sep '
                          'mtrr pge mca cmov pat pse36 clflush mmx fxsr '
                          'sse sse2 ht syscall nx rdtscp lm constant_tsc '
                          'rep_good nopl xtopology nonstop_tsc pni '
                          'pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic '
                          'movbe popcnt aes xsave avx rdrand hypervisor '
                          'lahf_lm abm 3dnowprefetch fsgsbase avx2 '
                          'invpcid rdseed clflushopt'),
                      ('cpu', 'logical', 'number', 2),
                      ('numa', 'nodes', 'count', 1),
                      ('numa', 'node_0', 'cpu_count', 2),
                      ('numa', 'node_0', 'cpu_mask', '0x3')]


GET_CPUS_AARCH64_RESULT = [('cpu', 'physical', 'number', 4),
                           ('cpu', 'physical_0', 'vendor', 'APM'),
                           ('cpu', 'physical_0', 'product', 'X-Gene'),
                           ('cpu', 'physical_0', 'cores', 2),
                           ('cpu', 'physical_0', 'threads', 2),
                           ('cpu', 'physical_0', 'model', 0),
                           ('cpu', 'physical_0', 'stepping', 0),
                           ('cpu', 'physical_0', 'l1d cache', 'unknown size'),
                           ('cpu', 'physical_0', 'l1i cache', 'unknown size'),
                           ('cpu', 'physical_0', 'l2 cache', 'unknown size'),
                           ('cpu', 'physical_0', 'flags',
                            'fp asimd evtstrm cpuid'),
                           ('cpu', 'physical_1', 'vendor', 'APM'),
                           ('cpu', 'physical_1', 'product', 'X-Gene'),
                           ('cpu', 'physical_1', 'cores', 2),
                           ('cpu', 'physical_1', 'threads', 2),
                           ('cpu', 'physical_1', 'model', 0),
                           ('cpu', 'physical_1', 'stepping', 0),
                           ('cpu', 'physical_1', 'l1d cache', 'unknown size'),
                           ('cpu', 'physical_1', 'l1i cache', 'unknown size'),
                           ('cpu', 'physical_1', 'l2 cache', 'unknown size'),
                           ('cpu', 'physical_1', 'flags',
                            'fp asimd evtstrm cpuid'),
                           ('cpu', 'physical_2', 'vendor', 'APM'),
                           ('cpu', 'physical_2', 'product', 'X-Gene'),
                           ('cpu', 'physical_2', 'cores', 2),
                           ('cpu', 'physical_2', 'threads', 2),
                           ('cpu', 'physical_2', 'model', 0),
                           ('cpu', 'physical_2', 'stepping', 0),
                           ('cpu', 'physical_2', 'l1d cache', 'unknown size'),
                           ('cpu', 'physical_2', 'l1i cache', 'unknown size'),
                           ('cpu', 'physical_2', 'l2 cache', 'unknown size'),
                           ('cpu', 'physical_2', 'flags',
                            'fp asimd evtstrm cpuid'),
                           ('cpu', 'physical_3', 'vendor', 'APM'),
                           ('cpu', 'physical_3', 'product', 'X-Gene'),
                           ('cpu', 'physical_3', 'cores', 2),
                           ('cpu', 'physical_3', 'threads', 2),
                           ('cpu', 'physical_3', 'model', 0),
                           ('cpu', 'physical_3', 'stepping', 0),
                           ('cpu', 'physical_3', 'l1d cache', 'unknown size'),
                           ('cpu', 'physical_3', 'l1i cache', 'unknown size'),
                           ('cpu', 'physical_3', 'l2 cache', 'unknown size'),
                           ('cpu', 'physical_3', 'flags',
                            'fp asimd evtstrm cpuid'),
                           ('cpu', 'logical', 'number', 8),
                           ('numa', 'nodes', 'count', 1),
                           ('numa', 'node_0', 'cpu_count', 8),
                           ('numa', 'node_0', 'cpu_mask', 'ff')]


GET_CPUS_PPC64LE = [('cpu', 'physical', 'number', 2),
                    ('cpu', 'physical_0', 'product',
                     'POWER9, altivec supported'),
                    ('cpu', 'physical_0', 'cores', 18),
                    ('cpu', 'physical_0', 'threads', 72),
                    ('cpu', 'physical_0', 'model', '2.2 (pvr 004e 1202)'),
                    ('cpu', 'physical_0', 'l1d cache', '32K'),
                    ('cpu', 'physical_0', 'l1i cache', '32K'),
                    ('cpu', 'physical_0', 'l2 cache', '512K'),
                    ('cpu', 'physical_0', 'l3 cache', '10240K'),
                    ('cpu', 'physical_0', 'min_Mhz', 2300.0),
                    ('cpu', 'physical_0', 'max_Mhz', 3800.0),
                    ('cpu', 'physical_1', 'product',
                     'POWER9, altivec supported'),
                    ('cpu', 'physical_1', 'cores', 18),
                    ('cpu', 'physical_1', 'threads', 72),
                    ('cpu', 'physical_1', 'model', '2.2 (pvr 004e 1202)'),
                    ('cpu', 'physical_1', 'l1d cache', '32K'),
                    ('cpu', 'physical_1', 'l1i cache', '32K'),
                    ('cpu', 'physical_1', 'l2 cache', '512K'),
                    ('cpu', 'physical_1', 'l3 cache', '10240K'),
                    ('cpu', 'physical_1', 'min_Mhz', 2300.0),
                    ('cpu', 'physical_1', 'max_Mhz', 3800.0),
                    ('cpu', 'logical', 'number', 144),
                    ('numa', 'nodes', 'count', 6),
                    ('numa', 'node_0', 'cpu_count', 72),
                    ('numa', 'node_0', 'cpu_mask', 'ffffffffffffffffff'),
                    ('numa', 'node_8', 'cpu_count', 72),
                    ('numa', 'node_8', 'cpu_mask',
                     'ffffffffffffffffff000000000000000000'),
                    ('numa', 'node_252', 'cpu_count', 0),
                    ('numa', 'node_252', 'cpu_mask', '0'),
                    ('numa', 'node_253', 'cpu_count', 0),
                    ('numa', 'node_253', 'cpu_mask', '0'),
                    ('numa', 'node_254', 'cpu_count', 0),
                    ('numa', 'node_254', 'cpu_mask', '0'),
                    ('numa', 'node_255', 'cpu_count', 0),
                    ('numa', 'node_255', 'cpu_mask', '0')]


DETECT_SYSTEM3_RESULT = [('system', 'product', 'serial', 'Empty'),
                         ('system', 'product', 'name', 'S2915'),
                         ('system', 'product', 'vendor',
                          'Tyan Computer Corporation'),
                         ('system', 'product', 'version', 'REFERENCE'),
                         ('system', 'product', 'uuid',
                          '83462C81-52BA-11CB-870F'),
                         ('system', 'motherboard', 'name', 'S2915'),
                         ('system', 'motherboard', 'vendor',
                          'Tyan Computer Corporation'),
                         ('system', 'motherboard', 'version', 'REFERENCE'),
                         ('system', 'motherboard', 'serial', 'Empty'),
                         ('firmware', 'bios', 'version',
                          'v3.00.2915 (10/10/2008)'),
                         ('firmware', 'bios', 'vendor',
                          'Phoenix Technologies Ltd.'),
                         ('memory', 'total', 'size', '4294967296'),
                         ('memory', 'bank:0:0', 'description',
                          'DIMM Synchronous [empty]'),
                         ('memory', 'bank:0:0', 'slot', 'C0_DIMM0'),
                         ('memory', 'bank:0:1', 'description',
                          'DIMM Synchronous [empty]'),
                         ('memory', 'bank:0:1', 'slot', 'C0_DIMM1'),
                         ('memory', 'bank:0:2', 'size', '1073741824'),
                         ('memory', 'bank:0:2', 'description',
                          'DIMM Synchronous'),
                         ('memory', 'bank:0:2', 'slot', 'C0_DIMM2'),
                         ('memory', 'bank:0:3', 'size', '1073741824'),
                         ('memory', 'bank:0:3', 'description',
                          'DIMM Synchronous'),
                         ('memory', 'bank:0:3', 'slot', 'C0_DIMM3'),
                         ('memory', 'bank:0:4', 'description',
                          'DIMM Synchronous [empty]'),
                         ('memory', 'bank:0:4', 'slot', 'C0_DIMM0'),
                         ('memory', 'bank:0:5', 'description',
                          'DIMM Synchronous [empty]'),
                         ('memory', 'bank:0:5', 'slot', 'C1_DIMM1'),
                         ('memory', 'bank:0:6', 'size', '1073741824'),
                         ('memory', 'bank:0:6', 'description',
                          'DIMM Synchronous'),
                         ('memory', 'bank:0:6', 'slot', 'C1_DIMM2'),
                         ('memory', 'bank:0:7', 'size', '1073741824'),
                         ('memory', 'bank:0:7', 'description',
                          'DIMM Synchronous'),
                         ('memory', 'bank:0:7', 'slot', 'C1_DIMM3'),
                         ('memory', 'banks', 'count', '8'),
                         ('system', 'os', 'vendor', 'Ubuntu'),
                         ('system', 'os', 'version', 'Ubuntu 14.04 LTS'),
                         ('system', 'kernel', 'version', '3.13.0-24-generic'),
                         ('system', 'kernel', 'arch', 'x86_64'),
                         ('system', 'kernel', 'cmdline',
                          'BOOT_IMAGE=/boot/vmlinuz')]


DETECT_SYSTEM2_RESULT = [('system', 'product', 'serial', 'PB4F20N'),
                         ('system', 'product', 'name',
                          '2347GF8 (LENOVO_MT_2347)'),
                         ('system', 'product', 'vendor', 'LENOVO'),
                         ('system', 'product', 'version', 'ThinkPad T430'),
                         ('system', 'product', 'uuid',
                          '83462C81-52BA-11CB-870F'),
                         ('system', 'motherboard', 'name', '2347GF8'),
                         ('system', 'motherboard', 'vendor', 'LENOVO'),
                         ('system', 'motherboard', 'version', 'Not Defined'),
                         ('system', 'motherboard', 'serial', '1ZLMB31B1G6'),
                         ('firmware', 'bios', 'version', 'G1ET73WW (2.09 )'),
                         ('firmware', 'bios', 'date', '10/19/2012'),
                         ('firmware', 'bios', 'vendor', 'LENOVO'),
                         ('memory', 'total', 'size', '8589934592'),
                         ('memory', 'bank:0', 'size', '4294967296'),
                         ('memory', 'bank:0', 'clock', '1600000000'),
                         ('memory', 'bank:0', 'description',
                         'SODIMM DDR3 Synchrone 1600 MHz (0,6 ns)'),
                         ('memory', 'bank:0', 'vendor', 'Samsung'),
                         ('memory', 'bank:0', 'product', 'M471B5273CH0-CK0'),
                         ('memory', 'bank:0', 'serial', '1222BCCE'),
                         ('memory', 'bank:0', 'slot', 'ChannelA-DIMM0'),
                         ('memory', 'bank:1', 'size', '4294967296'),
                         ('memory', 'bank:1', 'clock', '1600000000'),
                         ('memory', 'bank:1', 'description',
                         'SODIMM DDR3 Synchrone 1600 MHz (0,6 ns)'),
                         ('memory', 'bank:1', 'vendor', 'Samsung'),
                         ('memory', 'bank:1', 'product', 'M471B5273CH0-CK0'),
                         ('memory', 'bank:1', 'serial', '1222BCA2'),
                         ('memory', 'bank:1', 'slot', 'ChannelB-DIMM0'),
                         ('memory', 'banks', 'count', '2'),
                         ('network', 'eth0', 'businfo', 'pci@0000:00:19.0'),
                         ('network', 'eth0', 'vendor', 'Intel Corporation'),
                         ('network', 'eth0', 'product',
                         '82579LM Gigabit Network Connection'),
                         ('network', 'eth0', 'firmware', '0.13-3'),
                         ('network', 'eth0', 'link', 'no'),
                         ('network', 'eth0', 'driver', 'e1000e'),
                         ('network', 'eth0', 'latency', '0'),
                         ('network', 'eth0', 'autonegotiation', 'on'),
                         ('network', 'eth0', 'serial', '00:21:cc:d9:bf:26'),
                         ('network', 'wlan0', 'businfo', 'pci@0000:03:00.0'),
                         ('network', 'wlan0', 'vendor', 'Intel Corporation'),
                         ('network', 'wlan0', 'product',
                         'Centrino Advanced-N 6205 [Taylor Peak]'),
                         ('network', 'wlan0', 'firmware', '18.168.6.1'),
                         ('network', 'wlan0', 'ipv4', '192.168.1.185'),
                         ('network', 'wlan0', 'ipv4-netmask', '255.255.255.0'),
                         ('network', 'wlan0', 'ipv4-cidr', '24'),
                         ('network', 'wlan0', 'ipv4-network', '192.168.1.0'),
                         ('network', 'wlan0', 'link', 'yes'),
                         ('network', 'wlan0', 'driver', 'iwlwifi'),
                         ('network', 'wlan0', 'latency', '0'),
                         ('network', 'wlan0', 'serial', '84:3a:4b:33:62:82'),
                         ('network', 'wwan0', 'firmware',
                         'Mobile Broadband Network Device'),
                         ('network', 'wwan0', 'link', 'no'),
                         ('network', 'wwan0', 'driver', 'cdc_ncm'),
                         ('network', 'wwan0', 'serial', '02:15:e0:ec:01:00'),
                         ('system', 'os', 'vendor', 'Ubuntu'),
                         ('system', 'os', 'version', 'Ubuntu 14.04 LTS'),
                         ('system', 'kernel', 'version', '3.13.0-24-generic'),
                         ('system', 'kernel', 'arch', 'x86_64'),
                         ('system', 'kernel', 'cmdline',
                          'BOOT_IMAGE=/boot/vmlinuz')]


DETECT_SYSTEM_RESULT = [('system', 'product', 'serial', 'C02JR02WF57J'),
                        ('system', 'product', 'name',
                         'MacBookAir5,2 (System SKU#)'),
                        ('system', 'product', 'vendor', 'Apple Inc.'),
                        ('system', 'product', 'version', '1.0'),
                        ('system', 'product', 'uuid',
                         '83462C81-52BA-11CB-870F'),
                        ('system', 'motherboard', 'name',
                         'Mac-2E6FAB96566FE58C'),
                        ('system', 'motherboard', 'vendor', 'Apple Inc.'),
                        ('system', 'motherboard', 'version', 'MacBookAir5,2'),
                        ('system', 'motherboard', 'serial',
                         'C02245301ZFF25WAT'),
                        ('firmware', 'bios', 'version',
                         'MBA51.88Z.00EF.B01.1207271122'),
                        ('firmware', 'bios', 'date', '07/27/2012'),
                        ('firmware', 'bios', 'vendor', 'Apple Inc.'),
                        ('memory', 'total', 'size', '8589934592'),
                        ('memory', 'bank:0', 'size', '4294967296'),
                        ('memory', 'bank:0', 'clock', '1600000000'),
                        ('memory', 'bank:0', 'description',
                        'SODIMM DDR3 Synchronous 1600 MHz (0,6 ns)'),
                        ('memory', 'bank:0', 'vendor',
                        'Hynix Semiconductor (Hyundai Electronics)'),
                        ('memory', 'bank:0', 'product', 'HMT451S6MFR8A-PB'),
                        ('memory', 'bank:0', 'serial', '0x00000000'),
                        ('memory', 'bank:0', 'slot', 'DIMM0'),
                        ('memory', 'bank:1', 'size', '4294967296'),
                        ('memory', 'bank:1', 'clock', '1600000000'),
                        ('memory', 'bank:1', 'description',
                        'SODIMM DDR3 Synchronous 1600 MHz (0,6 ns)'),
                        ('memory', 'bank:1', 'vendor',
                        'Hynix Semiconductor (Hyundai Electronics)'),
                        ('memory', 'bank:1', 'product', 'HMT451S6MFR8A-PB'),
                        ('memory', 'bank:1', 'serial', '0x00000000'),
                        ('memory', 'bank:1', 'slot', 'DIMM0'),
                        ('memory', 'banks', 'count', '2'),
                        ('network', 'vnet0', 'size', '10000000'),
                        ('network', 'vnet0', 'link', 'yes'),
                        ('network', 'vnet0', 'driver', 'tun'),
                        ('network', 'vnet0', 'duplex', 'full'),
                        ('network', 'vnet0', 'speed', '10Mbit/s'),
                        ('network', 'vnet0', 'autonegotiation', 'off'),
                        ('network', 'vnet0', 'serial', 'fe:54:00:c1:1a:f7'),
                        ('network', 'tap0', 'size', '10000000'),
                        ('network', 'tap0', 'ipv4', '10.152.18.103'),
                        ('network', 'tap0', 'ipv4-netmask', '255.255.255.0'),
                        ('network', 'tap0', 'ipv4-cidr', '24'),
                        ('network', 'tap0', 'ipv4-network', '10.152.18.0'),
                        ('network', 'tap0', 'link', 'yes'),
                        ('network', 'tap0', 'driver', 'tun'),
                        ('network', 'tap0', 'duplex', 'full'),
                        ('network', 'tap0', 'speed', '10Mbit/s'),
                        ('network', 'tap0', 'autonegotiation', 'off'),
                        ('network', 'tap0', 'serial', 'e2:66:69:22:be:fb'),
                        ('network', 'wlan0', 'firmware', 'N/A'),
                        ('network', 'wlan0', 'ipv4', '192.168.12.13'),
                        ('network', 'wlan0', 'ipv4-netmask', '255.255.255.0'),
                        ('network', 'wlan0', 'ipv4-cidr', '24'),
                        ('network', 'wlan0', 'ipv4-network', '192.168.12.0'),
                        ('network', 'wlan0', 'link', 'yes'),
                        ('network', 'wlan0', 'driver', 'brcmsmac'),
                        ('network', 'wlan0', 'serial', '00:88:65:35:2b:50'),
                        ('system', 'os', 'vendor', 'Ubuntu'),
                        ('system', 'os', 'version', 'Ubuntu 14.04 LTS'),
                        ('system', 'kernel', 'version', '3.13.0-24-generic'),
                        ('system', 'kernel', 'arch', 'x86_64'),
                        ('system', 'kernel', 'cmdline',
                         'BOOT_IMAGE=/boot/vmlinuz')]
