# 全部测评索引

由 `data/benchmarks.json` 生成。★ 是固定条件重复测试的优先候选，不代表一道题就能证明降智。状态与来源核验状态分开。

<a id="quick"></a>

## 快速检查与日常任务

| 测试／来源 | 测什么、怎么玩 | 如何判分 | 回归用途 | 门槛／当前状态 |
| --- | --- | --- | --- | --- |
| [洗车：走路还是开车](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/high-suite.json) | 目标理解与常识 | 带车去洗车且理由一致 | △ 辅助观察：热身／天花板；单次答错不作降智证据 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [时间计算与反附和](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/high-suite.json) | 识别错误前提、时间计算 | 9:40+35分钟=10:15并纠错 | △ 辅助观察：建议生成跨午夜新变体 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [只改指定时间](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/high-suite.json) | 精确编辑、保留无关字句 | 目标句逐字核对，内容与格式另报 | ★ 回归优先：低成本发现不遵守要求 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [多轮出游限制](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/high-suite.json) | 跨轮记忆与条件保留 | 四项原条件不漏、不编、不收紧 | ★ 回归优先：同轮数同历史，检查约束漂移 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [会议缺失信息不脑补](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/high-suite.json) | 忠实提取、未知信息 | 已有任务／人／时间一致；未知保留 | ★ 回归优先：语义事实与指定措辞分开看 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [满月夜，狼人还能上夜班吗？](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/playful-season.json) | 跨午夜时间边界、多个约束同时满足、禁止相邻连班 | 按冻结criteria/gates；参考解见公开任务包 | ★ 回归优先：开发题，需先校准难度与评分；不同协议分开 | 轻至中：约束问答；已有公开题面，未采集模型成绩；local-public-source |
| [修好机器人，别顺手把它重装了](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/playful-season.json) | 多位置局部编辑、保护无关内容、逐字执行 | 按冻结criteria/gates；参考解见公开任务包 | ★ 回归优先：开发题，需先校准难度与评分；不同协议分开 | 轻至中：约束问答；已有公开题面，未采集模型成绩；local-public-source |
| [房东改了三次条件，怪物还住得下吗？](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/playful-season.json) | 多轮状态更新、约束冲突识别、撤销旧条件 | 按冻结criteria/gates；参考解见公开任务包 | ★ 回归优先：开发题，需先校准难度与评分；不同协议分开 | 轻至中：约束问答；已有公开题面，未采集模型成绩；local-public-source |
| [外星人会议：谁又替同事答应了？](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/playful-season.json) | 冲突材料整合、版本优先级、证据引用、未知信息保留 | 按冻结criteria/gates；参考解见公开任务包 | ★ 回归优先：开发题，需先校准难度与评分；不同协议分开 | 轻至中：约束问答；已有公开题面，未采集模型成绩；local-public-source |
| [推老板进工位](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/short-challenges.json) | 不可逆动作、多步规划 | 模拟每步合法性、终态、步数；不是比对参考串 | ★ 回归优先：两张固定地图可回归，但题少应补变体 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [齿轮诈骗：能否转动与最小修复](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/short-challenges.json) | 拒绝不可行前提、图约束纠错 | 正反例；转向二分图、驱动连通、最少删边 | ★ 回归优先：含能转与不能转对照，避免一律否定 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [非传递骰子：后选反而占优](https://nrich.maths.org/problems/non-transitive-dice) | 概率枚举、非传递关系 | 枚举36点数组合；示例胜率5/9 | ★ 回归优先：经典题污染风险，新骰面先验算 | 轻至中：素材／评分准备另核；未在本仓库实测；historical-lead |

<a id="visual"></a>

## 视觉、图形与整活

| 测试／来源 | 测什么、怎么玩 | 如何判分 | 回归用途 | 门槛／当前状态 |
| --- | --- | --- | --- | --- |
| [鹈鹕骑自行车 SVG](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/high-suite.json) | 构图与身体／车架连接 | 安全SVG门槛与连接量表、人工核验 | △ 辅助观察：固定渲染和盲评；观感噪声大 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [辣椒炒肉账单整活](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/high-suite.json) | 视觉阅读与票据层级 | 按出题者1份约定；实际票据解释有争议 | — 不入核心回归：争议答案，不放核心回归 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [非洲草原奔跑斑马 SVG](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/high-suite.json) | 画图、多要素执行 | 条纹5／动作4／场景3／交付3 | △ 辅助观察：适合看作品，不宜单图排名 | 轻：短问答／素材另备；已有公开实测；本轮未重跑；local-public-source |
| [章鱼搬家：最近的门，根本挤不过去](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/playful-season.json) | 图关系、通行约束、最短路径与SVG忠实表达 | 按冻结criteria/gates；参考解见公开任务包 | △ 辅助观察：开发题，需先校准难度与评分；不同协议分开 | 中：多轮／人工核验；已有公开题面，未采集模型成绩；local-public-source |
| [鹈鹕骑车：脚可别从踏板上飞走了](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/playful-season.json) | 跨时间的空间连接、脚踏联动、腿部弯伸、连续循环动画 | 按冻结criteria/gates；参考解见公开任务包 | △ 辅助观察：开发题，需先校准难度与评分；不同协议分开 | 中：多轮／人工核验；已有公开题面，未采集模型成绩；local-public-source |
| [VLMBias：反常动物数腿](https://github.com/anvo25/vlms-are-biased) | 视觉证据能否压过常识 | 数可见腿／图案；正常反常成对 | ★ 回归优先：新图+清晰无遮挡，分别计数和格式 | 轻至中：素材／评分准备另核；未在本仓库实测；reviewed-primary |
| [IllusionBench+：错觉反诈](https://github.com/mingZhang614/IllusionBench) | 真实长度判断、抗套路 | 本站改编建议保存几何真值；原项目评分另查 | ★ 回归优先：只用明确可量测子题；自建尺子题未实现 | 轻至中：素材／评分准备另核；未在本仓库实测；reviewed-primary |
| [MindTopo：羊圈缺口](https://github.com/mll-lab-nu/MindTopo) | 拓扑连通性、嵌套区域 | 按标注或生成环境判断能否逃出 | ★ 回归优先：固定图片，与开一处缺口的对照成对 | 轻至中：素材／评分准备另核；未在本仓库实测；reviewed-primary |
| [MET-Bench：图示三仙归洞](https://github.com/vanyacohen/MET-Bench) | 位置追踪、连续状态更新 | 交换记录推导最终目标位置 | ★ 回归优先：多序列，位置平衡；三选一猜中率1/3 | 轻至中：素材／评分准备另核；未在本仓库实测；reviewed-primary |
| [VET-Bench：动画三仙归洞](https://github.com/liutiedong/shellgame) | 遮挡后物体追踪 | 视频／帧序列与答案元数据核对 | △ 辅助观察：先确认视频或多图接口，别漏帧 | 轻至中：素材／评分准备另核；未在本仓库实测；reviewed-primary |
| [PHYRE／一球拆家](https://github.com/facebookresearch/phyre) | 碰撞、滚落与物理因果 | 模拟器接触成功；三选一中文题是未测改编 | △ 辅助观察：固定物理引擎、先排除边界不稳定场景 | 轻至中：素材／评分准备另核；未在本仓库实测；reviewed-primary |
| [DeepPHY](https://github.com/XinrunXu/DeepPHY) | 视觉物理动作选择 | 按环境结果验证放球动作 | △ 辅助观察：依赖环境；不冒充一轮聊天题 | 轻至中：素材／评分准备另核；未在本仓库实测；historical-lead |
| [WaldoBench：找摸鱼鹈鹕灵感](https://waldobench.com/) | 视觉搜索、多属性定位 | 坐标落目标框；目标缺失另测 | ★ 回归优先：原创动物图尚未制作；固定裁切／工具 | 轻至中：素材／评分准备另核；未在本仓库实测；historical-lead |
| [中文整活提示词合集](https://github.com/karminski/awesome-llm-benchmark-prompts) | 物理画面、动画、多约束生成 | 逐题冻结量表；合集本身不是统一评分基准 | △ 辅助观察：区分只给目标和完整技术指导 | 轻至中：素材／评分准备另核；未在本仓库实测；reviewed-primary |
| [玩具车跑步机淘汰赛](https://github.com/karminski/awesome-llm-benchmark-prompts/blob/main/instruction/prompt-car-crash.md) | 碰撞、多部件约束、画面稳定性 | 检查穿模、轮子作用、速度改变；需自建量表 | △ 辅助观察：物理逼真与好看分别评 | 轻至中：素材／评分准备另核；未在本仓库实测；historical-lead |
| [烤肉切片：旋转与状态守恒](https://www.reddit.com/r/LocalLLaMA/comments/1ua1na0/whats_more_impressive_glm_51_52_or_qwen_35_36/) | 动画、局部变化、状态一致性 | 原创加题：切片后肉柱减薄、盘子加一片 | △ 辅助观察：社区线索，尚无统一客观评分器 | 轻至中：素材／评分准备另核；未在本仓库实测；historical-lead |
| [原创：AI传话事故](https://github.com/mzh-nuist/ai-benchmark-index/blob/main/docs/IDEAS.md) | 角色、动作、因果信息保留 | 每棒按固定事实表核对丢失／新增 | △ 辅助观察：多模态、多模型混杂需控制 | 轻至中：素材／评分准备另核；未在本仓库实测；original-proposal |
| [原创：鹈鹕修车厂](https://github.com/mzh-nuist/ai-benchmark-index/blob/main/docs/IDEAS.md) | 定点维修、避免无关重画 | 同一坏图与冻结连接量表，前后对照 | △ 辅助观察：设计阶段，未实现统一评分器 | 轻至中：素材／评分准备另核；未在本仓库实测；original-proposal |

<a id="agent"></a>

## Agent、博弈与长任务

| 测试／来源 | 测什么、怎么玩 | 如何判分 | 回归用途 | 门槛／当前状态 |
| --- | --- | --- | --- | --- |
| [Agentic Pelican：看图返工](https://simonwillison.net/2025/Nov/11/agentic-pelican-on-a-bicycle/) | 视觉反馈、定位错误与有效修复 | 同一坏图、连接修复与无关内容保留 | △ 辅助观察：原实验与本站修车厂原创方案分开 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [TowerBench：搭高别倒](https://github.com/eanderson4/llm-bench-tower-building/releases/tag/main-1) | 空间规划、风险与收手 | 环境测最终站立高度，多种子 | △ 辅助观察：固定工具、预算、物理引擎 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [CoasterBench：造过山车](https://github.com/wseaton/CoasterBench) | 几何规划、工具反馈 | 游戏规则判断轨道和完成情况 | △ 辅助观察：复杂环境专项；先核可复现版本 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [Vending-Bench Arena：小卖部竞争](https://andonlabs.com/evals/vending-bench-arena) | 长期经营、谈判、记账 | 按多人经营规则；不能混单人榜 | △ 辅助观察：长时多Agent，非低成本日测 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [GPTNT：双AI拆弹](https://gptnt.github.io/) | 信息不对称、沟通与限时决策 | 游戏拆弹成功与合法行动 | △ 辅助观察：需游戏本体和环境；固定角色分工 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [Agents’ 100m：机器人跑百米](https://agents100m.com/) | 控制、试错和预算分配 | 仿真规则与比赛成绩，审查爬行策略是否合规 | △ 辅助观察：仿真和算力门槛高 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [Universal Paperclips Bench](https://github.com/bitnovus/universalpaperclipsbench) | 长期规划、资源调度、浏览器执行 | 游戏目标与阶段状态；保存全过程 | △ 辅助观察：数小时级线索，当前耗时未实测 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [BabaIsBench／Baba Is Harbor](https://github.com/stared/baba-is-harbor) | 改写规则、多步规划 | 引擎执行动作并判断通关 | △ 辅助观察：游戏本体、容器与工具预算一致 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [WitnessBench／外星厕所灵感](https://github.com/fleet-ai/witnessbench) | 主动探索、规则发现、迁移 | 试验次数、通关率、新关卡成功 | △ 辅助观察：厕所为原创皮肤，非原任务名称 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [Kitchen Rush：后厨打工](https://github.com/bassimeledath/kitchen-rush) | 调度、工具调用与时效 | 按订单交付及KR规则；固定延迟赛道 | △ 辅助观察：token折算时间不等于实时时延 | 重：环境与多轮预算另核；未在本仓库实测；reviewed-primary |
| [DuoCook：一模型指挥双厨师](https://arxiv.org/html/2610.31511v1) | 并行规划、资源冲突 | 按论文订单／合法动作等规则 | △ 辅助观察：未核到完整可运行包，只索引论文 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [Overcooked-Bench：四人后厨](https://www.turinggames.ai/evals/overcooked-bench) | 多Agent协作与私人记忆 | 按项目规则；先核环境和运行入口 | △ 辅助观察：未确认开源runner，不称一键可跑 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [QUACK：鹅鸭杀](https://github.com/New-Ground-AI/QUACK) | 局部信息、记忆、博弈、证词一致性 | 日志核对行动和胜负；策略撒谎不一律扣分 | △ 辅助观察：可先看公开回放，重跑成本未知 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |
| [SpaceChem：工厂与程序规划候补](https://spacechem.wincon.dev/) | 长期程序规划 | 原站未充分核读，不转述二手分数 | — 不入核心回归：仅候补，不列已核验可复现 | 重：环境与多轮预算另核；未在本仓库实测；historical-lead |

<a id="standard"></a>

## 成熟 benchmark 与专项能力

| 测试／来源 | 测什么、怎么玩 | 如何判分 | 回归用途 | 门槛／当前状态 |
| --- | --- | --- | --- | --- |
| [IFEval](https://github.com/google-research/google-research/tree/master/instruction_following_eval) | 可验证指令遵循 | 规则strict／loose，无模型裁判 | ★ 回归优先：小集固定；中文改编需新验证器 | 轻；未在本仓库实测；reviewed-primary |
| [FollowBench](https://github.com/YJiangcm/FollowBench) | 中英文多约束执行 | 官方GPT-4裁判，HSR／SSR／CSL | ★ 回归优先：裁判本身有波动和费用 | 中；未在本仓库实测；reviewed-primary |
| [GSM-Symbolic](https://github.com/apple-aiml-research/ml-gsm-symbolic) | 数学模板与数字变体稳定性 | 数值核对与答案抽取；生成器未确认发布 | ★ 回归优先：固定模板多个实例；非一道口算 | 轻至中；未在本仓库实测；reviewed-primary |
| [LiveBench 传统套件／1.x](https://github.com/LiveBench/LiveBench) | 数学、代码、语言、推理等 | 按任务核对；2.0长任务不混算 | △ 辅助观察：固定release，不拿换题掉分当降智 | 中至重；未在本仓库实测；reviewed-primary |
| [SimpleQA](https://github.com/openai/simple-evals/blob/main/simpleqa_eval.py) | 短事实问答、正确／错／不答 | 官方模型裁判；非纯字符串比较 | △ 辅助观察：固定联网与裁判，人工抽核 | 中；未在本仓库实测；reviewed-primary |
| [RULER](https://github.com/NVIDIA/RULER) | 长上下文检索、跟踪与聚合 | 生成、预测、脚本核验 | ★ 回归优先：固定长度／tokenizer／种子，截断另记 | 中至重；未在本仓库实测；reviewed-primary |
| [BFCL](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard) | 工具选择、参数、调用与多轮 | AST／执行等按类别判断 | ★ 回归优先：固定版本与工具schema，不简化成JSON题 | 中；未在本仓库实测；reviewed-primary |
| [SWE-bench Verified](https://github.com/SWE-bench/SWE-bench) | 真实仓库issue修复 | 容器中跑任务测试 | △ 辅助观察：固定Agent／工具／预算和镜像 | 重；未在本仓库实测；reviewed-primary |
| [Terminal-Bench 1.x／2.0分开](https://github.com/harbor-framework/terminal-bench-1) | 终端Agent端到端任务 | 沙箱测试；2.0用Harbor另列版本 | △ 辅助观察：不适合聊天框一道题检验 | 重；未在本仓库实测；reviewed-primary |
| [τ-bench 历史版](https://github.com/sierra-research/tau-bench) | 用户／Agent／政策与工具交互 | 环境目标与pass^k一致成功率 | △ 辅助观察：旧任务已过时，新τ³协议另查 | 重；未在本仓库实测；reviewed-primary |
| [OCRBench v1](https://github.com/Yuliang-Liu/MultimodalOCR/tree/main/OCRBench) | OCR、文档问答、信息抽取 | 官方脚本；v2不混算 | ★ 回归优先：固定图像字节／分辨率／裁切 | 轻至中；未在本仓库实测；reviewed-primary |
| [MathVista](https://github.com/lupantech/MathVista) | 图形图表数学推理 | 官方支持LLM答案抽取再计算 | △ 辅助观察：固定split、OCR辅助与抽取器 | 中；未在本仓库实测；reviewed-primary |
| [Vending-Bench／2](https://andonlabs.com/evals/vending-bench-2) | 库存、定价、长期经营一致性 | 环境账户余额；开源runner未核实 | △ 辅助观察：长任务专项；与Arena不同 | 重；未在本仓库实测；reviewed-primary |
| [鹈鹕原始实验（Simon Willison）](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/) | SVG作品、构图与连接关系 | 人工比较，无统一客观综合分 | △ 辅助观察：公开多年，记忆风险；固定量表 | 轻至中；未在本仓库实测；reviewed-primary |
| [ARC-AGI-1](https://github.com/fchollet/ARC-AGI) | 抽象网格规则归纳 | 输出网格精确匹配；限定尝试数 | △ 辅助观察：与ARC-AGI-2分开，公开题有污染风险 | 中至重；未在本仓库实测；reviewed-primary |
| [C-Eval](https://github.com/hkust-nlp/ceval) | 中文多学科知识 | 选择题自动计分 | △ 辅助观察：题目较老，不能概括写作与Agent | 轻至中；未在本仓库实测；reviewed-primary |
| [ModelTest 核心24题试点](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/core.json) | 内容、输出合同与完整交付 | 18自动／6人工；未校准区分度 | △ 辅助观察：规则与人工分开，不当已验证强模型基准 | 按子集与协议；费用未测；公开历史／方法目录；本轮未运行；local-public-source |
| [ModelTest Challenge V2公开开发集](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/challenge.json) | 数学、编码、推理、中文等候选任务 | 内容0–100、格式、严格交付分开 | △ 辅助观察：72项目录仅24道公开开发题，封存48项只有元数据 | 按子集与协议；费用未测；公开历史／方法目录；本轮未运行；local-public-source |
| [ModelTest 速度／TPS协议](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/runner/measurement.py) | 正文TPS、首内容／首正文／完整耗时 | 检查可靠usage、块边界和最小采样条件 | — 不入核心回归：速度变化不是降智；推理token不能当正文 | 按子集与协议；费用未测；公开历史／方法目录；本轮未运行；local-public-source |
| [ModelTest 25项能力体系](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/dist/data/framework.json) | 能力、性能、成本与可靠性指标方法 | 逐项方法与实现状态，不是统一满分题库 | △ 辅助观察：并发、pass@1等未接入不冒充已测 | 按子集与协议；费用未测；公开历史／方法目录；本轮未运行；local-public-source |
| [ModelTest 三道长输出采样题](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/datasets/speed_tasks.json) | 持续输出及传输速度 | 按测量协议，不按chunk数量估token | — 不入核心回归：只做速度采样，不能判能力退化 | 按子集与协议；费用未测；公开历史／方法目录；本轮未运行；local-public-source |
| [ModelTest 历史30题起步集](https://github.com/mzh-nuist/modeltest/blob/6b745dbc5fcd8627b9b3fe2f45acdf41561619fb/datasets/tasks.json) | 多方向基础任务与人工项 | exact／contains／JSON／人工待评 | △ 辅助观察：历史开发材料，难度未校准 | 按子集与协议；费用未测；公开历史／方法目录；本轮未运行；local-public-source |
