# AI Benchmark Index · AI 测评与降智检查索引

**把成熟 benchmark、中文日常题和整活玩法放进一张能用的目录。重点找出模型是不是真的“不如以前好用”。**

[★ 先看降智检查](docs/REGRESSION.md) · [全部 60 项](INDEX.md) · [16 道自有题与评分](docs/OWN-TESTS.md) · [原始来源核查](research/primary-sources.md) · [ModelTest 网站与答卷](https://modeltest.cc/)

收录 **16 道自有公开测试＋5 套自有历史／专项测试目录＋39 个外部评测项目**。这里既有 IFEval、GSM-Symbolic、BFCL、SWE-bench，也有羊圈诈骗、三仙归洞、推老板、鹈鹕、AI 后厨和小卖部。不是权威排行榜，不给没有实测的项目编分数。

## 收录边界

核心索引只收录 AI 能力评测集、回归测试题库与评测执行／检查脚本。终端信息流、个人浏览器插件和无关效率工具不收录；纯创意、资料框架与待核实线索留在[候补文档](docs/IDEAS.md)，按[贡献指南](CONTRIBUTING.md)审核后才能进入核心。

## 我就想知道 AI 有没有变笨，先看什么？

| 现象 | 推荐入口 | 为什么 |
| --- | --- | --- |
| 不听要求，擅自改一大段 | [定点改字／机器人维修](docs/OWN-TESTS.md)、[IFEval](https://github.com/google-research/google-research/tree/master/instruction_following_eval) | 有具体约束，可核验漏改、误改和格式 |
| 明明错了还顺着你说 | [齿轮诈骗](https://modeltest.cc/#checkup/season/gear-scam)、[GSM-Symbolic](https://github.com/apple-aiml-research/ml-gsm-symbolic) | 错误前提与正常对照一起测，避免只会一律否定 |
| 聊几轮就忘条件 | [出游记忆／怪物合租](docs/OWN-TESTS.md)、[RULER](https://github.com/NVIDIA/RULER) | 看条件保留、更新与撤销，不只复述关键词 |
| 缺信息却开始编 | [会议未知项／冲突纪要](docs/OWN-TESTS.md) | 可直接对照原材料；格式与事实错误分开 |
| 看图总凭常识猜 | [VLMBias](https://github.com/anvo25/vlms-are-biased)、[错觉反诈](https://github.com/mingZhang614/IllusionBench)、[羊圈](https://github.com/mll-lab-nu/MindTopo) | 用图中真值和正反例检查；中文改编需另备素材 |
| 计划挺好，执行就翻车 | [推老板](https://modeltest.cc/#checkup/season/boss-sokoban)、[BFCL](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard) | 用模拟器／工具执行结果判分，不听模型自夸 |

**一道题错了只是案例。** 固定服务商、模型快照、系统提示、推理预算、上下文、工具和评分器，再用同题多次成对比较，才有条件判断服务表现是否持续下降。[完整方法与记录模板](docs/REGRESSION.md)

## 怎么读目录

| 标记 | 含义 |
| --- | --- |
| ★ 回归优先 | 适合准备固定变体，重复检查特定能力；是本索引建议，未证明对所有模型都有区分度 |
| △ 辅助观察 | 有趣或有专项价值，但人工判分、长任务成本或环境影响较大 |
| — 不入核心回归 | 争议答案或来源／实现核查不足，保留线索但不据此下结论 |

索引分四类：[快速日常题](INDEX.md#quick)、[视觉与整活](INDEX.md#visual)、[Agent 长任务](INDEX.md#agent)、[成熟基准](INDEX.md#standard)。来源核验状态、历史实测状态、回归建议互相独立。

## 仓库里有什么

```text
INDEX.md                       按方向分类的完整中文索引
data/benchmarks.json            60项机器可读目录
data/modeltest-tasks.json       16道公开原题、参考与评分字段
docs/OWN-TESTS.md               能直接阅读的原题和判分说明
docs/REGRESSION.md              降智回归检查方法与排错顺序
docs/IDEAS.md                   原创改编与待核实线索
docs/PROVENANCE.md              来源、许可、状态和边界
research/primary-sources.md     16项成熟来源的逐项核查
templates/                     单次记录与前后比较模板
scripts/                       搜索、生成、离线校验与可用性检查
```

自有题来自 [ModelTest 公开源码](https://github.com/mzh-nuist/modeltest) 的固定快照，保留原题、参考、评分与来源摘要。原网站里的模型成绩仍留在原项目；新一期开发题与已采集旧题分开标记。这个索引本轮新增模型调用 **0 次**。

## 本地使用

需要 Python 3.12+，无需第三方包或 API 密钥。

```bash
git clone https://github.com/mzh-nuist/ai-benchmark-index.git
cd ai-benchmark-index
python scripts/search.py --regression priority
python scripts/search.py --category visual
python scripts/search.py 记忆
python scripts/build_index.py --check
python scripts/validate.py
```

正式测试前先按[前置环境诊断](docs/REGRESSION.md)检查模型标识、接入状态和服务策略；目录查询通过不等于推理可用或底层身份已证实。

修改 `data/benchmarks.json` 后，运行 `python scripts/build_index.py` 更新 Markdown。CI 只做离线验证，不调用被测模型。

## 来源与贡献

材料结合了「规划 AI 模型测评网站」和「寻找好玩又测智能的AI测评」两个工作流；不上传聊天全文。优先链接原作者、官方代码和数据卡，未重新核验的旧线索明确标记 `historical-lead`。[来源说明](docs/PROVENANCE.md)

欢迎补充原始链接、短题、程序判分器和失败案例。请按 [贡献指南](CONTRIBUTING.md) 提供能力目标、明确判据、复现条件、污染风险和原始出处，不把宣传分数当作自己的实测。

新增代码 MIT，原创索引说明 CC BY 4.0；第三方材料遵守原许可，见 [LICENSE](LICENSE)。作者：[逐风03 / mzh-nuist](https://github.com/mzh-nuist)。
