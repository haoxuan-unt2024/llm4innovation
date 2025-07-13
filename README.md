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

### Scientific Literature Quality Assessment

#### Benchmarks

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


