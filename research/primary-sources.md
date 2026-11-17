# 外部基准一手来源核查

核查日期：2026-11-17。范围：16 个外部基准/实验来源；仅浏览官方仓库、作者项目页、官方数据卡或原论文。未调用商业模型、未运行这些基准，也未复核排行榜分数。以下运行负担是依据任务形态和依赖作出的定性判断，不是实测时间、token 或价格承诺。

## 如何使用这份索引

建议先链接上游，保存中文说明和自建评测协议，不整包搬运题库或素材。仓库代码许可、数据许可、原始图片/题目许可可能不同；本页提供核对入口，不把“公开可读”等同于允许任意再分发。

“回归适配”指可否固定样本、配置和评分方法重复运行，不表示上游已经证明某个在线服务发生降级。单题失败、单次低分或一张图只能形成案例。判断服务质量变化，应固定题目版本、模型标识、访问路由、系统提示、采样与推理预算、工具、上下文和评分器，多次成对比较；模型版本更新应明确列为比较因素。版本/后端无法锁定时，结论限于该访问入口在该时间段的表现。下面的优先级均为本索引的编辑判断。

| 负担 | 本页含义 |
| --- | --- |
| 低 | 单轮文本/单图小样本可做；仍有模型生成成本 |
| 中 | 多约束、多图、判分模型或多轮工具使成本增加 |
| 高 | 长上下文、容器环境、多轮 Agent、长时模拟或大规模采样；不建议默认日常全量运行 |

## 01 · IFEval

- **能力与来源**：检查明确、可验证的指令约束，例如关键词、格式和长度；官方入口为 [Google Research 子目录及 README](https://github.com/google-research/google-research/tree/master/instruction_following_eval)，数据说明见 [google/IFEval 官方数据卡](https://huggingface.co/datasets/google/IFEval/blob/main/README.md)。
- **评分/操作**：先收集 prompt/response JSONL，运行规则验证器；提供 strict 和 loose 评分，**无需 LLM 裁判**。[官方评分代码](https://github.com/google-research/google-research/blob/master/instruction_following_eval/evaluation_main.py)
- **回归适配/负担（判断）**：优先；小样本低负担，适合每日格式与约束回归。英语单词数和字符等规则不可直接当成中文规则；自行翻译或改验证器需要新协议版本。
- **许可入口**：[官方数据卡](https://huggingface.co/datasets/google/IFEval/blob/main/README.md)声明数据 Apache-2.0；代码仍核对仓库 LICENSE 和文件头。

## 02 · FollowBench

- **能力与来源**：逐级增加约束，观察约束满足和连续满足水平；作者提供中英文数据及流程。[官方仓库](https://github.com/YJiangcm/FollowBench)
- **评分/操作**：官方 README 的评估流程使用 GPT-4 作 LLM 裁判，指标含 HSR、SSR、CSL；不能列作纯确定性验证。[官方运行说明](https://github.com/YJiangcm/FollowBench/blob/master/README.md)
- **回归适配/负担（判断）**：优先关注中文版本；中负担，生成与裁判均需预算。裁判快照、提示、原始打分都必须固定和保留；手工抽查裁判不一致。
- **许可入口**：[LICENSE](https://github.com/YJiangcm/FollowBench/blob/master/LICENSE)，仓库标示 Apache-2.0。

## 03 · GSM-Symbolic

- **能力与来源**：用数学文字题模板及数字/条件变体观察推理稳定性；官方仓库包含 GSM-Symbolic、P1、P2 的模板和已生成数据。[Apple 官方仓库](https://github.com/apple-aiml-research/ml-gsm-symbolic)、[Apple 研究页](https://machinelearning.apple.com/research/gsm-symbolic)
- **评分/操作**：本次读到的 README 明确说 parser/data generator 尚未发布；不要把模板文件说成现成的一键生成器。可针对已发布数据自行适配最终答案抽取、数值核对，并检查抽取失败。[README](https://github.com/apple-aiml-research/ml-gsm-symbolic/blob/main/README.md)
- **回归适配/负担（判断）**：优先；固定少量模板及其多个实例为低至中负担。报告同模板不同实例的波动，避免只挑一道错题或只报平均分。
- **许可入口**：[Apple LICENSE](https://github.com/apple-aiml-research/ml-gsm-symbolic/blob/main/LICENSE)为自定义条款，不写成 MIT/Apache；另查 ACKNOWLEDGEMENTS 及原始 GSM 数据来源。

## 04 · LiveBench（明确区分版本）

- **能力与来源**：传统 LiveBench 套件覆盖数学、代码、推理、语言、指令和数据分析，并以可核对答案自动判分；[官方仓库 README](https://github.com/LiveBench/LiveBench/blob/main/README.md)描述这套流程。[官方首页](https://livebench.ai/)本次已显示 LiveBench 2.0 长时任务，不能把首页的新定义与旧仓库协议拼成一个基准。
- **评分/操作**：旧套件支持生成、判断和结果展示，按任务/发布批次选择；代码任务可能额外需要执行环境，Agent 代码任务需要 Docker。[官方 README](https://github.com/LiveBench/LiveBench/blob/main/README.md)
- **回归适配/负担（判断）**：中至高；固定 release 和任务小集做回归，同时单列新发布题检查过拟合。不同发布题集的总分不直接解释为模型变强/变弱。
- **许可入口**：[代码 LICENSE](https://github.com/LiveBench/LiveBench/blob/main/LICENSE)为 Apache-2.0；各任务数据、上游来源及 2.0 内容需另查，不由代码许可统一覆盖。

## 05 · SimpleQA

- **能力与来源**：短答案事实准确性；官方实现将回答分为正确、错误和未尝试。[OpenAI simple-evals](https://github.com/openai/simple-evals)、[SimpleQA 评分源码](https://github.com/openai/simple-evals/blob/main/simpleqa_eval.py)
- **评分/操作**：使用 grader_model 判断，不是简单字符串完全匹配；源码支持重复采样。若改用自建字符串规则或人工评分，需披露协议改变。[评分源码](https://github.com/openai/simple-evals/blob/main/simpleqa_eval.py)
- **回归适配/负担（判断）**：中；可固定小集，但要控制联网能力与裁判配置，按拒答/错误/正确分别报告。事实问答结果不能外推为通用推理能力。
- **许可入口**：[simple-evals LICENSE](https://github.com/openai/simple-evals/blob/main/LICENSE)为 MIT；数据下载地址和适用声明由评分代码及发布材料继续核对，不能仅凭代码许可推断全部题目版权。

## 06 · RULER

- **能力与来源**：可配置长度、复杂度的合成长上下文任务，覆盖检索之外的跟踪、聚合等能力。[NVIDIA 官方仓库](https://github.com/NVIDIA/RULER)、[运行 README](https://github.com/NVIDIA/RULER/blob/main/README.md)
- **评分/操作**：生成合成输入、调用模型、执行评估脚本；固定生成配置、随机种子、tokenizer 和序列长度。属于可脚本化评估。[官方仓库 scripts](https://github.com/NVIDIA/RULER/tree/main/scripts)
- **回归适配/负担（判断）**：短档中、长档高；适合固定多个长度档观察掉点。务必记录是否截断、实际输入长度、max output 与缓存；长度增加时失败不等于服务在时间上降级。
- **许可入口**：[LICENSE](https://github.com/NVIDIA/RULER/blob/main/LICENSE)为 Apache-2.0；生成时所用背景文本等上游材料仍查其来源。

## 07 · Berkeley Function Calling Leaderboard（BFCL）

- **能力与来源**：工具选择、参数和可执行调用；版本从单轮扩展至多轮，以及 V4 的搜索/记忆/格式敏感性。[官方子目录](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)、[官方数据卡](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard)
- **评分/操作**：按类别采用 AST/执行等检查；生成和评估分离，可指定类别和题目。不可把整个 BFCL 简化为一个 JSON 格式测验。[README](https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/README.md)
- **回归适配/负担（判断）**：单轮小集低至中，多轮/搜索更高。固定 schema、模型调用适配器、并行工具能力、搜索结果/记忆状态及版本；联网工具结果变化需单独分析。
- **许可入口**：[Gorilla LICENSE](https://github.com/ShishirPatil/gorilla/blob/main/LICENSE)及[官方数据卡](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard)均给出 Apache-2.0；额外服务遵循自身条款。

## 08 · SWE-bench Verified

- **能力与来源**：给定真实代码仓库和 issue，生成修复补丁；Verified 是经过工程师核对的子集，不代表所有隐藏测试完美或结果绝无污染。[官方文档](https://www.swebench.com/SWE-bench/)、[官方 Verified 数据集](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified)
- **评分/操作**：Docker 环境应用补丁并执行测试；模型/Agent 生成补丁与 harness 判分是不同步骤。[官方仓库](https://github.com/SWE-bench/SWE-bench)
- **回归适配/负担（判断）**：高；需容器、依赖和较长轨迹。固定 Agent scaffold、可见文件、检索、工具和预算，环境构建/超时单列，不能全归因于基础模型。
- **许可入口**：[harness LICENSE](https://github.com/SWE-bench/SWE-bench/blob/main/LICENSE)为 MIT；原项目代码、补丁和 issue 的许可/来源另查，不能套用 harness 许可打包再分发。

## 09 · Terminal-Bench（1.x / 2.0 分开）

- **能力与来源**：终端环境中的端到端 Agent 任务；原仓库现重定向为 [terminal-bench-1](https://github.com/harbor-framework/terminal-bench-1)，其 README 推荐新用户使用 [Harbor](https://github.com/harbor-framework/harbor)运行 Terminal-Bench 2.0。
- **评分/操作**：连接 Agent 与终端沙箱，任务测试脚本检查结果；需要安装环境并选择 Agent 适配。单纯把题目发给聊天框并非完整 Terminal-Bench。[1.x README](https://github.com/harbor-framework/terminal-bench-1/blob/main/README.md)
- **回归适配/负担（判断）**：高；记录任务包、镜像、harness、Agent 和资源限制。主要适合专项周期回归，不列成“几分钟就能检测所有模型降级”。
- **许可入口**：[1.x LICENSE](https://github.com/harbor-framework/terminal-bench-1/blob/main/LICENSE)为 Apache-2.0；Harbor、2.0 任务和镜像需各查自身许可。

## 10 · τ-bench（历史版本）

- **能力与来源**：用户模拟器、Agent、工具和行业政策的动态交互；[原官方仓库](https://github.com/sierra-research/tau-bench)。本次官方 README 警告旧航空/零售任务已过时，导向 [tau2-bench 仓库中的 τ³-bench](https://github.com/sierra-research/tau2-bench)。
- **评分/操作**：运行交互轨迹并按任务检查；原版提供 pass^k 关注多次运行的一致成功，区别于“多试几次至少成功一次”的 pass@k。[原版 README](https://github.com/sierra-research/tau-bench/blob/main/README.md)
- **回归适配/负担（判断）**：高；至少包括被测 Agent 与用户模拟器调用。固定模拟器和环境状态，多轮策略/预算也要一致；新旧 τ 任务不能混算同一总分。
- **许可入口**：[原版 LICENSE](https://github.com/sierra-research/tau-bench/blob/main/LICENSE)为 MIT；新版与新增领域核对其独立仓库及数据声明。

## 11 · OCRBench（v1；v2 单列）

- **能力与来源**：文字识别、场景文字问答、文档问答、关键信息抽取和手写公式识别。[官方 OCRBench 子目录](https://github.com/Yuliang-Liu/MultimodalOCR/tree/main/OCRBench)、[原版 README](https://github.com/Yuliang-Liu/MultimodalOCR/blob/main/OCRBench/README.md)
- **评分/操作**：有模型脚本和评测入口，README 也指向 VLMEvalKit/lmms-eval；新模型需要适配。标注经过人工核验，不等于每次运行靠人工判分。[官方评测说明](https://github.com/Yuliang-Liu/MultimodalOCR/tree/main/OCRBench#evaluation)
- **回归适配/负担（判断）**：小图集低至中；固定图片原字节、分辨率、裁切、压缩和图像 detail 参数，分别报告场景/文档/手写。原仓库另有 v2，分数不可混用。
- **许可入口**：[代码 LICENSE.txt](https://github.com/Yuliang-Liu/MultimodalOCR/blob/main/LICENSE.txt)为 MIT；汇集图片及原始数据集的许可需逐来源核对。

## 12 · MathVista

- **能力与来源**：视觉情境中的数学推理，包含图表、几何与其他视觉题。[官方仓库](https://github.com/lupantech/MathVista)、[官方项目页](https://mathvista.github.io/)
- **评分/操作**：官方流程为回答生成、答案抽取、归一化计算分数；答案抽取提供 LLM 方法，不能把整条管线称为无模型裁判依赖。[官方 evaluation 说明](https://github.com/lupantech/MathVista#-evaluations-on-mathvista)
- **回归适配/负担（判断）**：中；记录 testmini/test 子集、图像预处理、是否额外提供 OCR/图片描述、答案抽取器；小样本不能冒称完整 MathVista 分数。
- **许可入口**：[官方许可说明](https://github.com/lupantech/MathVista#-license)：新贡献 CC BY-SA 4.0，原图和题目归原作者；另规定测试集用途与不用于训练。不能用一个“开源”标签覆盖所有素材。

## 13 · Vending-Bench / Vending-Bench 2

- **能力与来源**：长期经营模拟中的库存、采购、定价与一致性；[原作者项目页](https://andonlabs.com/evals/vending-bench)与[现行 Vending-Bench 2 页](https://andonlabs.com/evals/vending-bench-2)。2 的指标为模拟一年后的账户余额。
- **评分/操作**：模拟器可记账评分；本轮只核实公开项目说明，**未核实到可直接采用的官方开源 runner/数据许可**，不标成已可本地一键复现。猜测的 `AndonLabs/vending-bench` GitHub 地址返回 404，不作为入口。
- **回归适配/负担（判断）**：高；适合研究长时漂移和多次运行方差，日常低成本检查可借鉴任务思想自行设计短版，但不得叫作完整 Vending-Bench 分数。
- **许可入口**：本次项目页未确认代码/环境再分发许可；维持链接引用。原版、2 与 Arena 是不同协议，不合并排行榜。

## 14 · Pelican riding a bicycle（Simon Willison）

- **能力与来源**：让文本模型生成“鹈鹕骑自行车”的 SVG，用可见产物观察构图、代码和视觉关系。[作者原文](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/)、[作者仓库](https://github.com/simonw/pelican-bicycle)
- **评分/操作**：脚本可批量生成，观感通常靠人工比较；上游未提供统一的客观综合分。它是个人实验/展示题，不能与正式多题基准的统计证据等同。
- **回归适配/负担（判断）**：生成低、人工比较另算；适合内容展示及案例回归。需要固定提示、渲染器、画布与盲评表，并多次采样；现在已广泛公开，不能延续作者 2024 年对“可能未进训练集”的猜测为当前保证。
- **许可入口**：[作者仓库](https://github.com/simonw/pelican-bicycle)本次页面未见 LICENSE；只链接，未经确认不复制整批 SVG/脚本并改挂本仓库许可。

## 15 · ARC-AGI-1

- **能力与来源**：少量网格示例中的抽象规则归纳和精确输出；[François Chollet 官方仓库](https://github.com/fchollet/ARC-AGI)。仓库明确标题为 ARC-AGI-1，并链接 ARC-AGI-2，版本需区分。
- **评分/操作**：输出网格可精确核对；仓库含任务与人类交互界面，不等同于自带完整 LLM Agent runner。尝试次数是协议的一部分。[官方说明](https://github.com/fchollet/ARC-AGI/blob/master/README.md)
- **回归适配/负担（判断）**：纯直接回答可低至中；程序搜索/多次候选可能高。固定网格编码、示例、候选次数、求解工具和预算。公开题反复调参会污染评估；自建变体不自动等价于官方 ARC 分数。
- **许可入口**：[LICENSE](https://github.com/fchollet/ARC-AGI/blob/master/LICENSE)为 Apache-2.0；竞赛私有测试及其他版本规则另查。

## 16 · C-Eval

- **能力与来源**：中文多学科、多难度选择题，适合作为中文知识覆盖的一个维度。[官方仓库](https://github.com/hkust-nlp/ceval)、[官方网站](https://cevalbenchmark.com/)
- **评分/操作**：官方提供评测代码和使用说明；按选择题答案自动计分。固定 split、few-shot 数、示例、答题模板及选项抽取方式。[README](https://github.com/hkust-nlp/ceval/blob/main/README.md)
- **回归适配/负担（判断）**：固定分学科小集低，全量中；不代表中文写作、交互或实际工具能力。题目公开较久，需要注意训练暴露与分数饱和；本轮不据此认定任何模型污染。
- **许可入口**：[代码 LICENSE](https://github.com/hkust-nlp/ceval/blob/main/LICENSE)为 MIT；[LICENSE-DATA](https://github.com/hkust-nlp/ceval/blob/main/LICENSE-DATA)与 README 明确数据为 CC BY-NC-SA 4.0，代码/数据分开标注。

## 作为日常回归包的选择（编辑建议，尚未运行）

1. 先组合 IFEval 的规则约束、GSM-Symbolic 的同模板变体、BFCL 的离线单轮小集，以及自有 ModelTest 中已经锁定答案/评分器的短题；视觉另建固定 OCR 小集。
2. 中文约束可引入 FollowBench 中文版，但保留裁判依赖。真实事实类用 SimpleQA 单独观察；不把它与规则判断混成一个不透明总分。
3. RULER 按长度分档定期测；SWE-bench、Terminal-Bench、τ 与 Vending 类作为有预算和环境准备的专项。Pelican 用于可视案例，并明确人工主观维度。

这些建议只确定选型；本仓库没有因此获得上游全部数据的再分发权，也没有任何本轮新测模型成绩。

## 降级结论所需的最小证据（本索引的方法建议）

- **先固定比较对象**：同模型快照/别名、同服务商和实际路由、地区/账户档位、工具状态、系统提示、模型参数、推理预算、上下文、题集/评分器版本；无法固定的字段写明未知。
- **同题成对、多次重跑**：预先固定抽样与主要指标，比较每题的前后变化；同时报告样本数、重复次数、方差/区间、错题明细和请求失败，不用最好一次对最差一次。随机性存在时，温度为零也不视作完全确定。
- **单列故障来源**：超时、限流、截断、拒答、格式解析失败、工具/搜索失败、评分器变化；先排查服务与评测环境，再讨论能力变化。不同模型版本或不同工具预算可以比较，但不能称为“同条件服务降级”。
- **控制污染**：公开题只测已知题表现；保留独立的新题或生成变体作交叉检查，并检查模板和答案。变体必须单列协议版本，不悄悄与旧分数合并。
- **先预算后执行**：区分被测模型调用、裁判、模拟用户、工具服务、图像和长上下文；预设样本/轮数/时间上限。运行前检查脚本会否自动调用模型；本轮未做任何付费调用。
- **结论用语分级**：“某次失败案例”→“固定题集上的稳定分数变化”→“该服务入口在受控条件下的性能变化”；不从某道陷阱题跃迁到“模型全面变笨”或断言供应商故意减配。

本文件只核实来源与使用边界，不对上述项目排名、最新得分、运行可用性或完整许可证兼容性作未经运行/审计的保证。
