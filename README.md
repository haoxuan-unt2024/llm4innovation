# The Evolving Role of Large Language Models in Scientific Innovation: Evaluator, Collaborator, and Scientist

Scientific innovation is undergoing a paradigm shift driven by the rapid advancement of Large Language Models (LLMs). As science faces mounting challenges including information overload, disciplinary silos, and diminishing returns on conventional research methods, LLMs are emerging as powerful agents capable not only of enhancing scientific workflows but also of participating in and potentially leading the innovation process. Existing surveys mainly focus on different perspectives, phrases, and tasks in scientific research and discovery, while they have limitations in understanding the transformative potential and role differentiation of LLM. This survey proposes a comprehensive framework to categorize the evolving roles of LLMs in scientific innovation across three hierarchical levels: Evaluator, Collaborator, and Scientist. We distinguish between LLMs’ contributions to structured scientific research processes and open-ended scientific discovery, thereby offering a unified taxonomy that clarifies capability boundaries, evaluation criteria, and human-AI interaction patterns at each level. Through an extensive analysis of current methodologies, benchmarks, systems, and evaluation metrics, this survey delivers an in-depth and systematic synthesis on LLM-driven scientific innovation. We present LLMs not only as tools for automating existing processes, but also as catalysts capable of reshaping the epistemological foundations of science itself. This survey offers conceptual clarity, practical guidance, and theoretical foundations for future research, while also highlighting open challenges and ethical considerations in the pursuit of increasingly autonomous AI-driven science.

<img width="823" height="362" alt="Screenshot 2025-07-13 at 2 41 32 PM" src="https://github.com/user-attachments/assets/9f889e1f-b076-47be-8c9a-e814a5177249" />

Figure 3. The pyramidal framework of large language models' roles in scientific innovation: evaluators, collaborators, scientists.

## Contents

*   [Level 1: LLMs as Evaluators](#level-1-LLMs-as-Evaluators)
    *   [Scientific Knowledge Synthesis](#Scientific-Knowledge-Synthesis)
    *   [Scientific Literature Quality Assessment](#Scientific-Literature-Quality-Assessment)
*   [Level 2: LLMs as Collaborators](#level-2-LLMs-as-Collaborators)
    *   [Hypothesis Generation](#Hypothesis-Generation)
    *   [Experimental Assistant](#Experimental-Assistant)
*   [Level 3: LLMs as Scientists](#level-3-LLMs-as-Scientists)
    *   [Autonomous Scientific Research](#Autonomous-Scientific-Research)
    *   [Autonomous Scientific Discovery](#Autonomous-Scientific-Discovery)
 
## Level 1: LLMs as Evaluators

<img width="768" height="343" alt="Screenshot 2025-07-13 at 2 49 29 PM" src="https://github.com/user-attachments/assets/75a7a0b0-fc18-4be0-8e0c-47280c5180f4" />

Figure 5: Closed-loop workflow of LLMs as Evaluators. Multimodal embeddings underpin SKS (blue) and SLQA (green), whose outputs mutually reinforce each other and update the shared database.

### Scientific Knowledge Synthesis

#### Benchmarks

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<div class="csl-bib-body" style="line-height: 2; ">
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">1.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Burgess, J. <i>et al.</i> MicroVQA: A Multimodal Reasoning Benchmark for Microscopy-Based Scientific Research. <i>arXiv preprint arXiv:2503.13399</i> (2025).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=MicroVQA%3A%20A%20Multimodal%20Reasoning%20Benchmark%20for%20Microscopy-Based%20Scientific%20Research&amp;rft.jtitle=arXiv%20preprint%20arXiv%3A2503.13399&amp;rft.aufirst=James&amp;rft.aulast=Burgess&amp;rft.au=James%20Burgess&amp;rft.au=Jeffrey%20J%20Nirschl&amp;rft.au=Laura%20Bravo-S%C3%A1nchez&amp;rft.au=Alejandro%20Lozano&amp;rft.au=Sanket%20Rajan%20Gupte&amp;rft.au=Jesus%20G%20Galaz-Montoya&amp;rft.au=Yuhui%20Zhang&amp;rft.au=Yuchang%20Su&amp;rft.au=Disha%20Bhowmik&amp;rft.au=Zachary%20Coman&amp;rft.au=undefined&amp;rft.date=2025"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">2.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Cui, H. <i>et al.</i> CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning. in <i>The Thirteenth International Conference on Learning Representations</i> (2025).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=CURIE%3A%20Evaluating%20LLMs%20on%20Multitask%20Scientific%20Long-Context%20Understanding%20and%20Reasoning&amp;rft.btitle=The%20Thirteenth%20International%20Conference%20on%20Learning%20Representations&amp;rft.aufirst=Hao&amp;rft.aulast=Cui&amp;rft.au=Hao%20Cui&amp;rft.au=Zahra%20Shamsi&amp;rft.au=Gowoon%20Cheon&amp;rft.au=Xuejian%20Ma&amp;rft.au=Shutong%20Li&amp;rft.au=Maria%20Tikhanovskaya&amp;rft.au=Peter%20Christian%20Norgaard&amp;rft.au=Nayantara%20Mudur&amp;rft.au=Martyna%20Beata%20Plomecka&amp;rft.au=Paul%20Raccuglia&amp;rft.au=undefined&amp;rft.date=2025"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">3.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Huang, Z. <i>et al.</i> Olympicarena: Benchmarking multi-discipline cognitive reasoning for superintelligent ai. <i>Advances in Neural Information Processing Systems</i> <b>37</b>, 19209–19253 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Olympicarena%3A%20Benchmarking%20multi-discipline%20cognitive%20reasoning%20for%20superintelligent%20ai&amp;rft.jtitle=Advances%20in%20Neural%20Information%20Processing%20Systems&amp;rft.volume=37&amp;rft.aufirst=Zhen&amp;rft.aulast=Huang&amp;rft.au=Zhen%20Huang&amp;rft.au=Zengzhi%20Wang&amp;rft.au=Shijie%20Xia&amp;rft.au=Xuefeng%20Li&amp;rft.au=Haoyang%20Zou&amp;rft.au=Ruijie%20Xu&amp;rft.au=Run-Ze%20Fan&amp;rft.au=Lyumanshan%20Ye&amp;rft.au=Ethan%20Chern&amp;rft.au=Yixin%20Ye&amp;rft.au=undefined&amp;rft.date=2024&amp;rft.pages=19209%E2%80%9319253&amp;rft.spage=19209&amp;rft.epage=19253"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">4.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Li, L. <i>et al.</i> Multimodal ArXiv: A Dataset for Improving Scientific Comprehension of Large Vision-Language Models. in <i>Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</i> 14369–14387 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Multimodal%20ArXiv%3A%20A%20Dataset%20for%20Improving%20Scientific%20Comprehension%20of%20Large%20Vision-Language%20Models&amp;rft.btitle=Proceedings%20of%20the%2062nd%20Annual%20Meeting%20of%20the%20Association%20for%20Computational%20Linguistics%20(Volume%201%3A%20Long%20Papers)&amp;rft.aufirst=Lei&amp;rft.aulast=Li&amp;rft.au=Lei%20Li&amp;rft.au=Yuqi%20Wang&amp;rft.au=Runxin%20Xu&amp;rft.au=Peiyi%20Wang&amp;rft.au=Xiachong%20Feng&amp;rft.au=Lingpeng%20Kong&amp;rft.au=Qi%20Liu&amp;rft.date=2024&amp;rft.pages=14369%E2%80%9314387&amp;rft.spage=14369&amp;rft.epage=14387"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">5.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Lu, P. <i>et al.</i> MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts. in <i>The Twelfth International Conference on Learning Representations</i> (2023).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=MathVista%3A%20Evaluating%20Mathematical%20Reasoning%20of%20Foundation%20Models%20in%20Visual%20Contexts&amp;rft.btitle=The%20Twelfth%20International%20Conference%20on%20Learning%20Representations&amp;rft.aufirst=Pan&amp;rft.aulast=Lu&amp;rft.au=Pan%20Lu&amp;rft.au=Hritik%20Bansal&amp;rft.au=Tony%20Xia&amp;rft.au=Jiacheng%20Liu&amp;rft.au=Chunyuan%20Li&amp;rft.au=Hannaneh%20Hajishirzi&amp;rft.au=Hao%20Cheng&amp;rft.au=Kai-Wei%20Chang&amp;rft.au=Michel%20Galley&amp;rft.au=Jianfeng%20Gao&amp;rft.date=2023"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">6.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Lu, P. <i>et al.</i> Learn to explain: Multimodal reasoning via thought chains for science question answering. <i>Advances in Neural Information Processing Systems</i> <b>35</b>, 2507–2521 (2022).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Learn%20to%20explain%3A%20Multimodal%20reasoning%20via%20thought%20chains%20for%20science%20question%20answering&amp;rft.jtitle=Advances%20in%20Neural%20Information%20Processing%20Systems&amp;rft.volume=35&amp;rft.aufirst=Pan&amp;rft.aulast=Lu&amp;rft.au=Pan%20Lu&amp;rft.au=Swaroop%20Mishra&amp;rft.au=Tanglin%20Xia&amp;rft.au=Liang%20Qiu&amp;rft.au=Kai-Wei%20Chang&amp;rft.au=Song-Chun%20Zhu&amp;rft.au=Oyvind%20Tafjord&amp;rft.au=Peter%20Clark&amp;rft.au=Ashwin%20Kalyan&amp;rft.date=2022&amp;rft.pages=2507%E2%80%932521&amp;rft.spage=2507&amp;rft.epage=2521"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">7.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Pramanick, S., Chellappa, R. &amp; Venugopalan, S. SPIQA: A Dataset for Multimodal Question Answering on Scientific Papers. in <i>The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track</i> (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=SPIQA%3A%20A%20Dataset%20for%20Multimodal%20Question%20Answering%20on%20Scientific%20Papers&amp;rft.btitle=The%20Thirty-eight%20Conference%20on%20Neural%20Information%20Processing%20Systems%20Datasets%20and%20Benchmarks%20Track&amp;rft.aufirst=Shraman&amp;rft.aulast=Pramanick&amp;rft.au=Shraman%20Pramanick&amp;rft.au=Rama%20Chellappa&amp;rft.au=Subhashini%20Venugopalan&amp;rft.date=2024"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">8.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Rein, D. <i>et al.</i> Gpqa: A graduate-level google-proof q&amp;a benchmark. in <i>First Conference on Language Modeling</i> (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Gpqa%3A%20A%20graduate-level%20google-proof%20q%26a%20benchmark&amp;rft.btitle=First%20Conference%20on%20Language%20Modeling&amp;rft.aufirst=David&amp;rft.aulast=Rein&amp;rft.au=David%20Rein&amp;rft.au=Betty%20Li%20Hou&amp;rft.au=Asa%20Cooper%20Stickland&amp;rft.au=Jackson%20Petty&amp;rft.au=Richard%20Yuanzhe%20Pang&amp;rft.au=Julien%20Dirani&amp;rft.au=Julian%20Michael&amp;rft.au=Samuel%20R%20Bowman&amp;rft.date=2024"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">9.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Sun, L. <i>et al.</i> Scieval: A multi-level large language model evaluation benchmark for scientific research. in <i>Proceedings of the AAAI Conference on Artificial Intelligence</i> vol. 38 19053–19061 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1609%2Faaai.v38i17.29872&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Scieval%3A%20A%20multi-level%20large%20language%20model%20evaluation%20benchmark%20for%20scientific%20research&amp;rft.btitle=Proceedings%20of%20the%20AAAI%20Conference%20on%20Artificial%20Intelligence&amp;rft.aufirst=Liangtai&amp;rft.aulast=Sun&amp;rft.au=Liangtai%20Sun&amp;rft.au=Yang%20Han&amp;rft.au=Zihan%20Zhao&amp;rft.au=Da%20Ma&amp;rft.au=Zhennan%20Shen&amp;rft.au=Baocai%20Chen&amp;rft.au=Lu%20Chen&amp;rft.au=Kai%20Yu&amp;rft.date=2024&amp;rft.pages=19053%E2%80%9319061&amp;rft.spage=19053&amp;rft.epage=19061"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">10.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Wang, X. <i>et al.</i> SciBench: Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models. in <i>Forty-first International Conference on Machine Learning</i> (2023).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=SciBench%3A%20Evaluating%20College-Level%20Scientific%20Problem-Solving%20Abilities%20of%20Large%20Language%20Models&amp;rft.btitle=Forty-first%20International%20Conference%20on%20Machine%20Learning&amp;rft.aufirst=Xiaoxuan&amp;rft.aulast=Wang&amp;rft.au=Xiaoxuan%20Wang&amp;rft.au=Ziniu%20Hu&amp;rft.au=Pan%20Lu&amp;rft.au=Yanqiao%20Zhu&amp;rft.au=Jieyu%20Zhang&amp;rft.au=Satyen%20Subramaniam&amp;rft.au=Arjun%20R%20Loomba&amp;rft.au=Shichang%20Zhang&amp;rft.au=Yizhou%20Sun&amp;rft.au=Wei%20Wang&amp;rft.date=2023"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">11.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Yue, X. <i>et al.</i> Mmmu: A massive multi-discipline multimodal understanding and reasoning benchmark for expert agi. in <i>Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition</i> 9556–9567 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Mmmu%3A%20A%20massive%20multi-discipline%20multimodal%20understanding%20and%20reasoning%20benchmark%20for%20expert%20agi&amp;rft.btitle=Proceedings%20of%20the%20IEEE%2FCVF%20Conference%20on%20Computer%20Vision%20and%20Pattern%20Recognition&amp;rft.aufirst=Xiang&amp;rft.aulast=Yue&amp;rft.au=Xiang%20Yue&amp;rft.au=Yuansheng%20Ni&amp;rft.au=Kai%20Zhang&amp;rft.au=Tianyu%20Zheng&amp;rft.au=Ruoqi%20Liu&amp;rft.au=Ge%20Zhang&amp;rft.au=Samuel%20Stevens&amp;rft.au=Dongfu%20Jiang&amp;rft.au=Weiming%20Ren&amp;rft.au=Yuxuan%20Sun&amp;rft.au=undefined&amp;rft.date=2024&amp;rft.pages=9556%E2%80%939567&amp;rft.spage=9556&amp;rft.epage=9567"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">12.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Zhao, Y. <i>et al.</i> SciArena: An Open Evaluation Platform for Foundation Models in Scientific Literature Tasks. <i>arXiv preprint arXiv:2507.01001</i> (2025).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=SciArena%3A%20An%20Open%20Evaluation%20Platform%20for%20Foundation%20Models%20in%20Scientific%20Literature%20Tasks&amp;rft.jtitle=arXiv%20preprint%20arXiv%3A2507.01001&amp;rft.aufirst=Yilun&amp;rft.aulast=Zhao&amp;rft.au=Yilun%20Zhao&amp;rft.au=Kaiyan%20Zhang&amp;rft.au=Tiansheng%20Hu&amp;rft.au=Sihong%20Wu&amp;rft.au=Ronan%20Le%20Bras&amp;rft.au=Taira%20Anderson&amp;rft.au=Jonathan%20Bragg&amp;rft.au=Joseph%20Chee%20Chang&amp;rft.au=Jesse%20Dodge&amp;rft.au=Matt%20Latzke&amp;rft.au=undefined&amp;rft.date=2025"></span>
</div></body>
</html>



#### Algorithms

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

</head>
<body>
<div class="csl-bib-body" style="line-height: 2; ">
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">1.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Chao, W., Chen, M., Zhou, X. &amp; Luo, Z. A joint framework for identifying the type and arguments of scientific contribution. <i>Scientometrics</i> <b>128</b>, 3347–3376 (2023).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1007%2Fs11192-023-04694-6&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=A%20joint%20framework%20for%20identifying%20the%20type%20and%20arguments%20of%20scientific%20contribution&amp;rft.jtitle=Scientometrics&amp;rft.volume=128&amp;rft.issue=6&amp;rft.aufirst=Wenhan&amp;rft.aulast=Chao&amp;rft.au=Wenhan%20Chao&amp;rft.au=Mengyuan%20Chen&amp;rft.au=Xian%20Zhou&amp;rft.au=Zhunchen%20Luo&amp;rft.date=2023&amp;rft.pages=3347%E2%80%933376&amp;rft.spage=3347&amp;rft.epage=3376"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">2.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Dagdelen, J. <i>et al.</i> Structured information extraction from scientific text with large language models. <i>Nature Communications</i> <b>15</b>, 1418 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1038%2Fs41467-024-45563-x&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Structured%20information%20extraction%20from%20scientific%20text%20with%20large%20language%20models&amp;rft.jtitle=Nature%20Communications&amp;rft.volume=15&amp;rft.issue=1&amp;rft.aufirst=John&amp;rft.aulast=Dagdelen&amp;rft.au=John%20Dagdelen&amp;rft.au=Alexander%20Dunn&amp;rft.au=Sanghoon%20Lee&amp;rft.au=Nicholas%20Walker&amp;rft.au=Andrew%20S%20Rosen&amp;rft.au=Gerbrand%20Ceder&amp;rft.au=Kristin%20A%20Persson&amp;rft.au=Anubhav%20Jain&amp;rft.date=2024&amp;rft.pages=1418"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">3.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Hope, T. <i>et al.</i> SciSight: Combining faceted navigation and research group detection for COVID-19 exploratory scientific search. <i>Proceedings of the 2020 EMNLP (Systems Demonstrations), Association for Computational Linguistics</i> (2020).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=SciSight%3A%20Combining%20faceted%20navigation%20and%20research%20group%20detection%20for%20COVID-19%20exploratory%20scientific%20search&amp;rft.jtitle=Proceedings%20of%20the%202020%20EMNLP%20(Systems%20Demonstrations)%2C%20Association%20for%20Computational%20Linguistics&amp;rft.aufirst=Tom&amp;rft.aulast=Hope&amp;rft.au=Tom%20Hope&amp;rft.au=J%20Portenoy&amp;rft.au=K%20Vasan&amp;rft.au=J%20Borchardt&amp;rft.au=Eric%20Horvitz&amp;rft.au=DS%20Weld&amp;rft.au=MA%20Hearst&amp;rft.au=Jevin%20West&amp;rft.date=2020"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">4.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Jin, R. <i>et al.</i> Hegta: Leveraging heterogeneous graph-enhanced large language models for few-shot complex table understanding. in <i>Proceedings of the AAAI Conference on Artificial Intelligence</i> vol. 39 24294–24302 (2025).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Hegta%3A%20Leveraging%20heterogeneous%20graph-enhanced%20large%20language%20models%20for%20few-shot%20complex%20table%20understanding&amp;rft.btitle=Proceedings%20of%20the%20AAAI%20Conference%20on%20Artificial%20Intelligence&amp;rft.aufirst=Rihui&amp;rft.aulast=Jin&amp;rft.au=Rihui%20Jin&amp;rft.au=Yu%20Li&amp;rft.au=Guilin%20Qi&amp;rft.au=Nan%20Hu&amp;rft.au=Yuan-Fang%20Li&amp;rft.au=Jiaoyan%20Chen&amp;rft.au=Jianan%20Wang&amp;rft.au=Yongrui%20Chen&amp;rft.au=Dehai%20Min&amp;rft.au=Sheng%20Bi&amp;rft.date=2025&amp;rft.pages=24294%E2%80%9324302&amp;rft.spage=24294&amp;rft.epage=24302"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">5.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">La Quatra, M. &amp; Cagliero, L. Transformer-based highlights extraction from scientific papers. <i>Knowledge-Based Systems</i> <b>252</b>, 109382 (2022).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1016%2Fj.knosys.2022.109382&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Transformer-based%20highlights%20extraction%20from%20scientific%20papers&amp;rft.jtitle=Knowledge-Based%20Systems&amp;rft.volume=252&amp;rft.aufirst=Moreno&amp;rft.aulast=La%20Quatra&amp;rft.au=Moreno%20La%20Quatra&amp;rft.au=Luca%20Cagliero&amp;rft.date=2022&amp;rft.pages=109382"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">6.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Lahav, D. <i>et al.</i> A Search Engine for Discovery of Scientific Challenges and Directions. in <i>AAAI Conference on Artificial Intelligence</i> (2021). doi:<a href="https://doi.org/10.1609/aaai.v36i11.21456">https://doi.org/10.1609/aaai.v36i11.21456</a>.</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2Fhttps%3A%2F%2Fdoi.org%2F10.1609%2Faaai.v36i11.21456&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=A%20Search%20Engine%20for%20Discovery%20of%20Scientific%20Challenges%20and%20Directions&amp;rft.btitle=AAAI%20Conference%20on%20Artificial%20Intelligence&amp;rft.aufirst=Dan&amp;rft.aulast=Lahav&amp;rft.au=Dan%20Lahav&amp;rft.au=Jon%20Saad-Falcon&amp;rft.au=Bailey%20Kuehl&amp;rft.au=Sophie%20Johnson&amp;rft.au=Sravanthi%20Parasa&amp;rft.au=Noam%20Shomron&amp;rft.au=Duen%20Horng%20Chau&amp;rft.au=Diyi%20Yang&amp;rft.au=Eric%20Horvitz&amp;rft.au=Daniel%20S.%20Weld&amp;rft.au=Tom%20Hope&amp;rft.date=2021"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">7.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Ma, Y. <i>et al.</i> SciAgent: Tool-augmented Language Models for Scientific Reasoning. in <i>Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing</i> 15701–15736 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=SciAgent%3A%20Tool-augmented%20Language%20Models%20for%20Scientific%20Reasoning&amp;rft.btitle=Proceedings%20of%20the%202024%20Conference%20on%20Empirical%20Methods%20in%20Natural%20Language%20Processing&amp;rft.aufirst=Yubo&amp;rft.aulast=Ma&amp;rft.au=Yubo%20Ma&amp;rft.au=Zhibin%20Gou&amp;rft.au=Junheng%20Hao&amp;rft.au=Ruochen%20Xu&amp;rft.au=Shuohang%20Wang&amp;rft.au=Liangming%20Pan&amp;rft.au=Yujiu%20Yang&amp;rft.au=Yixin%20Cao&amp;rft.au=Aixin%20Sun&amp;rft.date=2024&amp;rft.pages=15701%E2%80%9315736&amp;rft.spage=15701&amp;rft.epage=15736"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">8.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Mondal, D., Modi, S., Panda, S., Singh, R. &amp; Rao, G. S. Kam-cot: Knowledge augmented multimodal chain-of-thoughts reasoning. in <i>Proceedings of the AAAI conference on artificial intelligence</i> vol. 38 18798–18806 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Kam-cot%3A%20Knowledge%20augmented%20multimodal%20chain-of-thoughts%20reasoning&amp;rft.btitle=Proceedings%20of%20the%20AAAI%20conference%20on%20artificial%20intelligence&amp;rft.aufirst=Debjyoti&amp;rft.aulast=Mondal&amp;rft.au=Debjyoti%20Mondal&amp;rft.au=Suraj%20Modi&amp;rft.au=Subhadarshi%20Panda&amp;rft.au=Rituraj%20Singh&amp;rft.au=Godawari%20Sudhakar%20Rao&amp;rft.date=2024&amp;rft.pages=18798%E2%80%9318806&amp;rft.spage=18798&amp;rft.epage=18806"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">9.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Prabhakar, V. <i>et al.</i> OmniScience: A Domain-Specialized LLM for Scientific Reasoning and Discovery. <i>arXiv preprint arXiv:2503.17604</i> (2025).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=OmniScience%3A%20A%20Domain-Specialized%20LLM%20for%20Scientific%20Reasoning%20and%20Discovery&amp;rft.jtitle=arXiv%20preprint%20arXiv%3A2503.17604&amp;rft.aufirst=Vignesh&amp;rft.aulast=Prabhakar&amp;rft.au=Vignesh%20Prabhakar&amp;rft.au=Md%20Amirul%20Islam&amp;rft.au=Adam%20Atanas&amp;rft.au=Yao-Ting%20Wang&amp;rft.au=Joah%20Han&amp;rft.au=Aastha%20Jhunjhunwala&amp;rft.au=Rucha%20Apte&amp;rft.au=Robert%20Clark&amp;rft.au=Kang%20Xu&amp;rft.au=Zihan%20Wang&amp;rft.au=undefined&amp;rft.date=2025"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">10.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Skarlinski, M. D. <i>et al.</i> Language agents achieve superhuman synthesis of scientific knowledge. <i>arXiv preprint arXiv:2409.13740</i> (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Language%20agents%20achieve%20superhuman%20synthesis%20of%20scientific%20knowledge&amp;rft.jtitle=arXiv%20preprint%20arXiv%3A2409.13740&amp;rft.aufirst=Michael%20D&amp;rft.aulast=Skarlinski&amp;rft.au=Michael%20D%20Skarlinski&amp;rft.au=Sam%20Cox&amp;rft.au=Jon%20M%20Laurent&amp;rft.au=James%20D%20Braza&amp;rft.au=Michaela%20Hinks&amp;rft.au=Michael%20J%20Hammerling&amp;rft.au=Manvitha%20Ponnapati&amp;rft.au=Samuel%20G%20Rodriques&amp;rft.au=Andrew%20D%20White&amp;rft.date=2024"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">11.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Song, Z., Hwang, G.-Y., Zhang, X., Huang, S. &amp; Park, B.-K. A scientific-article key-insight extraction system based on multi-actor of fine-tuned open-source large language models. <i>Scientific Reports</i> <b>15</b>, 1608 (2025).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1038%2Fs41598-025-85715-7&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=A%20scientific-article%20key-insight%20extraction%20system%20based%20on%20multi-actor%20of%20fine-tuned%20open-source%20large%20language%20models&amp;rft.jtitle=Scientific%20Reports&amp;rft.volume=15&amp;rft.issue=1&amp;rft.aufirst=Zihan&amp;rft.aulast=Song&amp;rft.au=Zihan%20Song&amp;rft.au=Gyo-Yeob%20Hwang&amp;rft.au=Xin%20Zhang&amp;rft.au=Shan%20Huang&amp;rft.au=Byung-Kwon%20Park&amp;rft.date=2025&amp;rft.pages=1608"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">12.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Wang, K. <i>et al.</i> MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning. in <i>12th International Conference on Learning Representations (ICLR 2024)</i> (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=MathCoder%3A%20Seamless%20Code%20Integration%20in%20LLMs%20for%20Enhanced%20Mathematical%20Reasoning&amp;rft.btitle=12th%20International%20Conference%20on%20Learning%20Representations%20(ICLR%202024)&amp;rft.aufirst=Ke&amp;rft.aulast=Wang&amp;rft.au=Ke%20Wang&amp;rft.au=Houxing%20Ren&amp;rft.au=Aojun%20Zhou&amp;rft.au=Zimu%20Lu&amp;rft.au=Sichun%20Luo&amp;rft.au=Weikang%20Shi&amp;rft.au=Renrui%20Zhang&amp;rft.au=Linqi%20Song&amp;rft.au=Mingjie%20Zhan&amp;rft.au=Hongsheng%20Li&amp;rft.date=2024"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">13.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Wang, L. <i>et al.</i> T-sciq: Teaching multimodal chain-of-thought reasoning via large language model signals for science question answering. in <i>Proceedings of the AAAI Conference on Artificial Intelligence</i> vol. 38 19162–19170 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=T-sciq%3A%20Teaching%20multimodal%20chain-of-thought%20reasoning%20via%20large%20language%20model%20signals%20for%20science%20question%20answering&amp;rft.btitle=Proceedings%20of%20the%20AAAI%20Conference%20on%20Artificial%20Intelligence&amp;rft.aufirst=Lei&amp;rft.aulast=Wang&amp;rft.au=Lei%20Wang&amp;rft.au=Yi%20Hu&amp;rft.au=Jiabang%20He&amp;rft.au=Xing%20Xu&amp;rft.au=Ning%20Liu&amp;rft.au=Hui%20Liu&amp;rft.au=Heng%20Tao%20Shen&amp;rft.date=2024&amp;rft.pages=19162%E2%80%9319170&amp;rft.spage=19162&amp;rft.epage=19170"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">14.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Wei, C.-H. <i>et al.</i> PubTator 3.0: an AI-powered literature resource for unlocking biomedical knowledge. <i>Nucleic Acids Research</i> <b>52</b>, W540–W546 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1093%2Fnar%2Fgkae235&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=PubTator%203.0%3A%20an%20AI-powered%20literature%20resource%20for%20unlocking%20biomedical%20knowledge&amp;rft.jtitle=Nucleic%20Acids%20Research&amp;rft.volume=52&amp;rft.issue=W1&amp;rft.aufirst=Chih-Hsuan&amp;rft.aulast=Wei&amp;rft.au=Chih-Hsuan%20Wei&amp;rft.au=Alexis%20Allot&amp;rft.au=Po-Ting%20Lai&amp;rft.au=Robert%20Leaman&amp;rft.au=Shubo%20Tian&amp;rft.au=Ling%20Luo&amp;rft.au=Qiao%20Jin&amp;rft.au=Zhizheng%20Wang&amp;rft.au=Qingyu%20Chen&amp;rft.au=Zhiyong%20Lu&amp;rft.date=2024-07-05&amp;rft.pages=W540-W546&amp;rft.spage=W540&amp;rft.epage=W546&amp;rft.issn=0305-1048%2C%201362-4962&amp;rft.language=en"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">15.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Zhang, D. <i>et al.</i> SciInstruct: A Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models. <i>Advances in Neural Information Processing Systems</i> <b>37</b>, 1443–1473 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=SciInstruct%3A%20A%20Self-Reflective%20Instruction%20Annotated%20Dataset%20for%20Training%20Scientific%20Language%20Models&amp;rft.jtitle=Advances%20in%20Neural%20Information%20Processing%20Systems&amp;rft.volume=37&amp;rft.aufirst=Dan&amp;rft.aulast=Zhang&amp;rft.au=Dan%20Zhang&amp;rft.au=Ziniu%20Hu&amp;rft.au=Sining%20Zhoubian&amp;rft.au=Zhengxiao%20Du&amp;rft.au=Kaiyu%20Yang&amp;rft.au=Zihan%20Wang&amp;rft.au=Yisong%20Yue&amp;rft.au=Yuxiao%20Dong&amp;rft.au=Jie%20Tang&amp;rft.date=2024&amp;rft.pages=1443%E2%80%931473&amp;rft.spage=1443&amp;rft.epage=1473"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">16.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Zhang, X. <i>et al.</i> MASSW: A new dataset and benchmark tasks for ai-assisted scientific workflows. <i>arXiv preprint arXiv:2406.06357</i> (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=MASSW%3A%20A%20new%20dataset%20and%20benchmark%20tasks%20for%20ai-assisted%20scientific%20workflows&amp;rft.jtitle=arXiv%20preprint%20arXiv%3A2406.06357&amp;rft.aufirst=Xingjian&amp;rft.aulast=Zhang&amp;rft.au=Xingjian%20Zhang&amp;rft.au=Yutong%20Xie&amp;rft.au=Jin%20Huang&amp;rft.au=Jinge%20Ma&amp;rft.au=Zhaoying%20Pan&amp;rft.au=Qijia%20Liu&amp;rft.au=Ziyang%20Xiong&amp;rft.au=Tolga%20Ergen&amp;rft.au=Dongsub%20Shim&amp;rft.au=Honglak%20Lee&amp;rft.au=undefined&amp;rft.date=2024"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">17.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Zhang, Z. <i>et al.</i> Multimodal Chain-of-Thought Reasoning in Language Models. <i>Transactions on Machine Learning Research</i> (2023).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Multimodal%20Chain-of-Thought%20Reasoning%20in%20Language%20Models&amp;rft.jtitle=Transactions%20on%20Machine%20Learning%20Research&amp;rft.aufirst=Zhuosheng&amp;rft.aulast=Zhang&amp;rft.au=Zhuosheng%20Zhang&amp;rft.au=Aston%20Zhang&amp;rft.au=Mu%20Li&amp;rft.au=George%20Karypis&amp;rft.au=Alex%20Smola&amp;rft.au=undefined&amp;rft.date=2023"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">18.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Zhang, Z. <i>et al.</i> Fine-grained information extraction from biomedical literature based on knowledge-enriched abstract meaning representation. in <i>Proc. The Joint Conference of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (ACL-IJCNLP 2021)</i> (2021). doi:<a href="https://doi.org/10.18653/v1/2021.acl-long.489">10.18653/v1/2021.acl-long.489</a>.</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.18653%2Fv1%2F2021.acl-long.489&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Fine-grained%20information%20extraction%20from%20biomedical%20literature%20based%20on%20knowledge-enriched%20abstract%20meaning%20representation&amp;rft.btitle=Proc.%20The%20Joint%20Conference%20of%20the%2059th%20Annual%20Meeting%20of%20the%20Association%20for%20Computational%20Linguistics%20and%20the%2011th%20International%20Joint%20Conference%20on%20Natural%20Language%20Processing%20(ACL-IJCNLP%202021)&amp;rft.aufirst=Zixuan&amp;rft.aulast=Zhang&amp;rft.au=Zixuan%20Zhang&amp;rft.au=Nikolaus%20Nova%20Parulian&amp;rft.au=Heng%20Ji&amp;rft.au=Ahmed%20S%20Elsayed&amp;rft.au=Skatje%20Myers&amp;rft.au=Martha%20Palmer&amp;rft.date=2021"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">19.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Zheng, Y. <i>et al.</i> Large language models for scientific synthesis, inference and explanation. <i>arXiv preprint arXiv:2310.07984</i> (2023).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Large%20language%20models%20for%20scientific%20synthesis%2C%20inference%20and%20explanation&amp;rft.jtitle=arXiv%20preprint%20arXiv%3A2310.07984&amp;rft.aufirst=Yizhen&amp;rft.aulast=Zheng&amp;rft.au=Yizhen%20Zheng&amp;rft.au=Huan%20Yee%20Koh&amp;rft.au=Jiaxin%20Ju&amp;rft.au=Anh%20TN%20Nguyen&amp;rft.au=Lauren%20T%20May&amp;rft.au=Geoffrey%20I%20Webb&amp;rft.au=Shirui%20Pan&amp;rft.date=2023"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">20.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Zhong, R. <i>et al.</i> Goal driven discovery of distributional differences via language descriptions. in <i>Proceedings of the 37th International Conference on Neural Information Processing Systems</i> 40204–40237 (2023).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Goal%20driven%20discovery%20of%20distributional%20differences%20via%20language%20descriptions&amp;rft.btitle=Proceedings%20of%20the%2037th%20International%20Conference%20on%20Neural%20Information%20Processing%20Systems&amp;rft.aufirst=Ruiqi&amp;rft.aulast=Zhong&amp;rft.au=Ruiqi%20Zhong&amp;rft.au=Peter%20Zhang&amp;rft.au=Steve%20Li&amp;rft.au=Jinwoo%20Ahn&amp;rft.au=Dan%20Klein&amp;rft.au=Jacob%20Steinhardt&amp;rft.date=2023&amp;rft.pages=40204%E2%80%9340237&amp;rft.spage=40204&amp;rft.epage=40237"></span>
</div></body>
</html>


### Scientific Literature Quality Assessment

#### Benchmarks

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

</head>
<body>
<div class="csl-bib-body" style="line-height: 2; ">
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">1.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Du, J. <i>et al.</i> LLMs Assist NLP Researchers: Critique Paper (Meta-) Reviewing. in <i>Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing</i> 5081–5099 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=LLMs%20Assist%20NLP%20Researchers%3A%20Critique%20Paper%20(Meta-)%20Reviewing&amp;rft.btitle=Proceedings%20of%20the%202024%20Conference%20on%20Empirical%20Methods%20in%20Natural%20Language%20Processing&amp;rft.aufirst=Jiangshu&amp;rft.aulast=Du&amp;rft.au=Jiangshu%20Du&amp;rft.au=Yibo%20Wang&amp;rft.au=Wenting%20Zhao&amp;rft.au=Zhongfen%20Deng&amp;rft.au=Shuaiqi%20Liu&amp;rft.au=Renze%20Lou&amp;rft.au=Henry%20Zou&amp;rft.au=Pranav%20Narayanan%20Venkit&amp;rft.au=Nan%20Zhang&amp;rft.au=Mukund%20Srinath&amp;rft.au=undefined&amp;rft.date=2024&amp;rft.pages=5081%E2%80%935099&amp;rft.spage=5081&amp;rft.epage=5099"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">2.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Dycke, N., Kuznetsov, I. &amp; Gurevych, I. NLPeer: A Unified Resource for the Computational Study of Peer Review. in <i>Annual Meeting of the Association for Computational Linguistics</i> (2022).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=NLPeer%3A%20A%20Unified%20Resource%20for%20the%20Computational%20Study%20of%20Peer%20Review&amp;rft.btitle=Annual%20Meeting%20of%20the%20Association%20for%20Computational%20Linguistics&amp;rft.aufirst=Nils&amp;rft.aulast=Dycke&amp;rft.au=Nils%20Dycke&amp;rft.au=Ilia%20Kuznetsov&amp;rft.au=Iryna%20Gurevych&amp;rft.date=2022"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">3.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Gao, Z., Brantley, K. &amp; Joachims, T. Reviewer2: Optimizing review generation through prompt generation. <i>arXiv preprint arXiv:2402.10886</i> (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Reviewer2%3A%20Optimizing%20review%20generation%20through%20prompt%20generation&amp;rft.jtitle=arXiv%20preprint%20arXiv%3A2402.10886&amp;rft.aufirst=Zhaolin&amp;rft.aulast=Gao&amp;rft.au=Zhaolin%20Gao&amp;rft.au=Kiant%C3%A9%20Brantley&amp;rft.au=Thorsten%20Joachims&amp;rft.date=2024"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">4.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Li, J., Yin, Y., Fortunato, S. &amp; Wang, D. A dataset of publication records for Nobel laureates. <i>Scientific data</i> <b>6</b>, 33 (2019).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1038%2Fs41597-019-0033-6&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=A%20dataset%20of%20publication%20records%20for%20Nobel%20laureates&amp;rft.jtitle=Scientific%20data&amp;rft.volume=6&amp;rft.issue=1&amp;rft.aufirst=Jichao&amp;rft.aulast=Li&amp;rft.au=Jichao%20Li&amp;rft.au=Yian%20Yin&amp;rft.au=Santo%20Fortunato&amp;rft.au=Dashun%20Wang&amp;rft.date=2019&amp;rft.pages=33"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">5.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Li, M., Hovy, E. H. &amp; Lau, J. H. Summarizing Multiple Documents with Conversational Structure for Meta-Review Generation. in <i>Conference on Empirical Methods in Natural Language Processing</i> (2023). doi:<a href="https://doi.org/10.18653/v1%2F2023.findings-emnlp.472">https://doi.org/10.18653/v1%2F2023.findings-emnlp.472</a>.</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2Fhttps%3A%2F%2Fdoi.org%2F10.18653%2Fv1%252F2023.findings-emnlp.472&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Summarizing%20Multiple%20Documents%20with%20Conversational%20Structure%20for%20Meta-Review%20Generation&amp;rft.btitle=Conference%20on%20Empirical%20Methods%20in%20Natural%20Language%20Processing&amp;rft.aufirst=Miao&amp;rft.aulast=Li&amp;rft.au=Miao%20Li&amp;rft.au=Eduard%20H.%20Hovy&amp;rft.au=Jey%20Han%20Lau&amp;rft.date=2023"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">6.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Lin, J., Song, J., Zhou, Z., Chen, Y. &amp; Shi, X. MOPRD: A multidisciplinary open peer review dataset. <i>Neural Computing and Applications</i> <b>35</b>, 24191–24206 (2022).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2Fhttps%3A%2F%2Fdoi.org%2F10.1007%2Fs00521-023-08891-5&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=MOPRD%3A%20A%20multidisciplinary%20open%20peer%20review%20dataset&amp;rft.jtitle=Neural%20Computing%20and%20Applications&amp;rft.volume=35&amp;rft.aufirst=Jialiang&amp;rft.aulast=Lin&amp;rft.au=Jialiang%20Lin&amp;rft.au=Jiaxin%20Song&amp;rft.au=Zhangping%20Zhou&amp;rft.au=Yidong%20Chen&amp;rft.au=X.%20Shi&amp;rft.date=2022&amp;rft.pages=24191-24206&amp;rft.spage=24191&amp;rft.epage=24206"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">7.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Lin, Z., Yin, Y., Liu, L. &amp; Wang, D. SciSciNet: A large-scale open data lake for the science of science research. <i>Scientific Data</i> <b>10</b>, 315 (2023).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1038%2Fs41597-023-02198-9&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=SciSciNet%3A%20A%20large-scale%20open%20data%20lake%20for%20the%20science%20of%20science%20research&amp;rft.jtitle=Scientific%20Data&amp;rft.volume=10&amp;rft.issue=1&amp;rft.aufirst=Zihang&amp;rft.aulast=Lin&amp;rft.au=Zihang%20Lin&amp;rft.au=Yian%20Yin&amp;rft.au=Lu%20Liu&amp;rft.au=Dashun%20Wang&amp;rft.date=2023&amp;rft.pages=315"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">8.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Mugabushaka, A.-M., Sadat, J. &amp; Faria, J. C. D. In Search of Outstanding Research Advances: Prototyping the creation of an open dataset of" editorial highlights". <i>arXiv preprint arXiv:2011.07910</i> (2020).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=In%20Search%20of%20Outstanding%20Research%20Advances%3A%20Prototyping%20the%20creation%20of%20an%20open%20dataset%20of%22%20editorial%20highlights%22&amp;rft.jtitle=arXiv%20preprint%20arXiv%3A2011.07910&amp;rft.aufirst=Alexis-Michel&amp;rft.aulast=Mugabushaka&amp;rft.au=Alexis-Michel%20Mugabushaka&amp;rft.au=Jasmin%20Sadat&amp;rft.au=Jorge%20Costa%20Dantas%20Faria&amp;rft.date=2020"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">9.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Xu, J. <i>et al.</i> PubMed knowledge graph 2.0: Connecting papers, patents, and clinical trials in biomedical science. <i>Scientific Data</i> <b>12</b>, 1–20 (2025).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1038%2Fs41597-025-05343-8&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=PubMed%20knowledge%20graph%202.0%3A%20Connecting%20papers%2C%20patents%2C%20and%20clinical%20trials%20in%20biomedical%20science&amp;rft.jtitle=Scientific%20Data&amp;rft.volume=12&amp;rft.issue=1&amp;rft.aufirst=Jian&amp;rft.aulast=Xu&amp;rft.au=Jian%20Xu&amp;rft.au=Chao%20Yu&amp;rft.au=Jiawei%20Xu&amp;rft.au=Vetle%20I%20Torvik&amp;rft.au=Jaewoo%20Kang&amp;rft.au=Mujeen%20Sung&amp;rft.au=Min%20Song&amp;rft.au=Yi%20Bu&amp;rft.au=Ying%20Ding&amp;rft.date=2025&amp;rft.pages=1%E2%80%9320&amp;rft.spage=1&amp;rft.epage=20"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">10.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Yuan, W., Liu, P. &amp; Neubig, G. Can we automate scientific reviewing? <i>Journal of Artificial Intelligence Research</i> <b>75</b>, 171–212 (2022).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_id=info%3Adoi%2F10.1613%2Fjair.1.12862&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=Can%20we%20automate%20scientific%20reviewing%3F&amp;rft.jtitle=Journal%20of%20Artificial%20Intelligence%20Research&amp;rft.volume=75&amp;rft.aufirst=Weizhe&amp;rft.aulast=Yuan&amp;rft.au=Weizhe%20Yuan&amp;rft.au=Pengfei%20Liu&amp;rft.au=Graham%20Neubig&amp;rft.date=2022&amp;rft.pages=171%E2%80%93212&amp;rft.spage=171&amp;rft.epage=212"></span>
  <div class="csl-entry" style="clear: left; ">
    <div class="csl-left-margin" style="float: left; padding-right: 0.5em;text-align: right; width: 1em;">11.</div><div class="csl-right-inline" style="margin: 0 .4em 0 1.5em;">Zhou, R., Chen, L. &amp; Yu, K. Is LLM a reliable reviewer? A comprehensive evaluation of LLM on automatic paper reviewing tasks. in <i>Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)</i> 9340–9351 (2024).</div>
  </div>
  <span class="Z3988" title="url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fzotero.org%3A2&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=proceeding&amp;rft.atitle=Is%20LLM%20a%20reliable%20reviewer%3F%20A%20comprehensive%20evaluation%20of%20LLM%20on%20automatic%20paper%20reviewing%20tasks&amp;rft.btitle=Proceedings%20of%20the%202024%20Joint%20International%20Conference%20on%20Computational%20Linguistics%2C%20Language%20Resources%20and%20Evaluation%20(LREC-COLING%202024)&amp;rft.aufirst=Ruiyang&amp;rft.aulast=Zhou&amp;rft.au=Ruiyang%20Zhou&amp;rft.au=Lu%20Chen&amp;rft.au=Kai%20Yu&amp;rft.date=2024&amp;rft.pages=9340%E2%80%939351&amp;rft.spage=9340&amp;rft.epage=9351"></span>
</div></body>
</html>

#### Algorithms

## Level 2: LLMs as Collaborators

<img width="563" height="358" alt="Screenshot 2025-07-13 at 2 57 39 PM" src="https://github.com/user-attachments/assets/c32ff8c4-d202-4468-a24e-821ca7b9adb7" />

Figure 6. LLMs as collaborators in scientific innovation. LLMs transforming raw knowledge into actionable hypotheses, designing and optimizing experiments, automating laboratory work, and rigorously analyzing results to drive continuous scientific innovation.
### Hypothesis Generation

#### Benchmarks



#### Algorithms

### Experimental Assistant

#### Benchmarks

#### Algorithms

## Level 3: LLMs as Scientists

<img width="587" height="551" alt="Screenshot 2025-07-13 at 2 58 34 PM" src="https://github.com/user-attachments/assets/9553aadc-0015-4dc3-8598-cb732de4a850" />

Figure 7. Taxonomy of LLMs as Scientists. The upper (blue) panel organizes ASR into three strata—fully autonomous end-to-end pipelines, closed-loop iterative research systems, and human-in-the-loop frameworks—each characterized by a distinct balance of speed, feedback integration, and expert oversight. The lower (yellow) panel groups ASR algorithms into multi-agent LLM laboratories and program-search/symbolic-reasoning approaches, highlighting their use of role-specialized agents, shared memories, external tool chains, and evolutionary routing for hypothesis generation and verification.

### Autonomous Scientific Research

#### Benchmarks

#### Algorithms

### Autonomous Scientific Discovery

#### Benchmarks

#### Algorithms


