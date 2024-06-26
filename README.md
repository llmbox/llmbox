## llmbox: 国产模型 OpenAI Assistant 兼容 API 

这是一个开源项目，旨在将国产语言模型与 OpenAI Assistant API 桥接，使开发者可以轻松地将国产模型集成到他们的应用程序中，并使用 OpenAI Assistant API 的便捷接口进行交互。

**为什么写这个项目**

- **降低LLM使用门槛:** 国产模型大都只提供了基础的chat api。需要使用者自己实现会话的管理，RAG等功能。提高了LLM的使用门槛。
- **找工作:** 拿这个项目做敲门砖。


**主要功能：**

- **无缝集成:** 提供与 OpenAI 的 Assistants API 完全兼容的 API，让开发者可以轻松地将国产模型集成到他们的现有工作流程中。
- **多轮对话:** 支持自然流畅的对话，无缝管理每个用户交互的上下文和历史记录。
- **检索增强生成 (RAG):** 利用外部知识来源增强国产模型的响应，提供更丰富、更有信息的答案。

**工作原理：**

1. **多轮对话管理:** 后端管理对话状态，为每个用户保留上下文和历史记录，确保对话连贯自然。
2. **RAG 集成:** 后端可以从外部知识来源（例如数据库、API）获取相关信息，并将其整合到模型的响应中。

**优势：**

- **易用性:** 无缝对接多个国产大模型
- **灵活性:** 提供熟悉的 OpenAI Assistant API 接口，简化了与现有应用程序的集成。
- **增强功能:** 利用多轮对话和 RAG 功能，丰富用户体验。
- **开源:** 促进社区协作和开发。

**入门指南：**

1. 部署应用程序：
    - 使用 Docker 构建镜像： `docker build -t llmbox .`
    - 运行容器： `docker run -p 8080:8080 llmbox`
2. 开始使用 OpenAI Assistant API 兼容接口：
    - 通过 `http://localhost:8080/v1/assistants` 接口进行请求。

**贡献：**

我们鼓励对该项目的贡献！欢迎提交错误修复、功能请求，甚至为其他国产模型添加新集成。

**免责声明:**

该项目与 OpenAI 无关。OpenAI Assistant API 的兼容性是为了方便起见，不应被误认为是与 OpenAI 服务的直接连接。

**敬请期待更多更新和激动人心的功能！**

