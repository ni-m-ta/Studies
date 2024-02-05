# Docker

**Docker** is an open-source platform that enables developers to automate the deployment of applications inside lightweight, portable containers. Containers are standalone, executable packages that include everything needed to run a piece of software, including the code, runtime, libraries, and system tools. Docker provides a consistent and reproducible environment across different machines, making it easier to develop, test, and deploy applications.

## Key Concepts:

1. **Containerization:**
   - Containers encapsulate an application and its dependencies, ensuring consistency across various environments. They are isolated from the host system and other containers.

2. **Docker Image:**
   - An image is a lightweight, standalone, and executable package that includes the application code, runtime, libraries, and other settings. Images serve as the blueprint for containers.

3. **Docker Container:**
   - A container is an instance of a Docker image. It runs as a process on the host machine, providing a consistent environment for the application to execute.

4. **Dockerfile:**
   - A Dockerfile is a script that defines the steps to create a Docker image. It includes instructions for configuring the base image, adding application code, setting environment variables, and more.

5. **Docker Hub:**
   - Docker Hub is a cloud-based registry that hosts Docker images. Developers can share and access pre-built images from Docker Hub, streamlining the deployment process.

6. **Docker Compose:**
   - Docker Compose is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure application services, networks, and volumes.

7. **Docker Swarm:**
   - Docker Swarm is a native clustering and orchestration solution for Docker. It allows users to create and manage a swarm of Docker nodes, making it easier to scale and manage containerized applications.

8. **Docker Engine:**
   - Docker Engine is the core component of Docker. It is a lightweight runtime and packaging tool for containers, providing the necessary functionalities to build, ship, and run containers.

## Workflow:
- Overviews:
    - Dockerfile -- build --> Docker image -- run --> Docker container <-- operations --> Docker compose

1. **Dockerfile Creation:**
   - Developers create a Dockerfile that specifies the configuration and dependencies for their application.

2. **Image Building:**
   - The Dockerfile is used to build a Docker image. The image contains the application and all necessary components.

3. **Image Distribution:**
   - Images can be stored in Docker Hub or other container registries, making them accessible to other developers and deployment environments.

4. **Containerization:**
   - Developers or operators deploy containers using the built images, ensuring consistent runtime environments.

5. **Orchestration (Optional):**
   - Docker Swarm or other orchestration tools can be used to manage and scale containerized applications across multiple hosts.

## Benefits:

1. **Consistency:**
   - Containers ensure consistency between development, testing, and production environments, reducing the "it works on my machine" problem.

2. **Isolation:**
   - Containers provide process and file system isolation, allowing multiple applications to run independently on the same host.

3. **Portability:**
   - Containers can run on any machine with Docker installed, making it easy to move applications between different environments.

4. **Resource Efficiency:**
   - Containers share the host OS kernel, resulting in faster startup times and efficient resource utilization compared to virtual machines.

5. **Scalability:**
   - Container orchestration tools enable easy scaling of applications by distributing containers across multiple hosts.

## Example Dockerfile:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

# Components
- Container
   - ソフトウェアパッケージを構築して実行できる、緩く分離された環境
   - イメージのメモリ内インスタンス
   - 欠点
      - コンテナストレージは一時的なもの
      - 元となるホストコンピューターと結合
      - ドライブのパフォーマンスが低下
   - ボリューム
      - 特定のフォルダーの場所にあるホストファイルシステムに格納
      - マウント後、これらのボリュームはホストコンピューターから分離
   - バインドマウント
      - 概念的にはボリュームと同じだが、特定のフォルダーを使うのではなく、ホスト上の任意のファイルまたはフォルダーをマウントできる
- Container Image
   - 任意のコンピューティング環境でアプリケーションを迅速かつ確実に実行するためのコードとすべての依存関係
   - ソフトウェアが含まれている移植可能なパッケージ
   - イメージを実行するとコンテナになる
   - Unionfs
      - ブランチと呼ばれる複数のディレクトリを内容がマージされているかのようにスタックできるファイルシステム
      - 内容は物理的に個別に保持
      - ファイルシステムを構築するときにブランチを追加及び削除できる
   - Basic Image
      - Dockerのscratchイメージを使用するイメージ
      - `scratch`
         - ファイルシステムレイヤーが作成されないされない空のコンテナイメージ
         - 実行するアプリケーションはホストOSカーネルを直接使用できることを想定
   - Pearent Image
      - イメージを作成するもとになるイメージ
   - Image tag
      - イメージのバージョンを管理するために使用されるテキスト文字列
- Docker Engine
   - クライアントとサーバーが同じホスト上で同時に実行されるクライアント/サーバーの実装として構成される、複数のコンポーネントで構成
   - クライアントは、サーバーとの通信に REST API を使用
- Docker Client
   - CLI
   - Docker Desktop
- Docker Server
   - dockerd
   - デーモン
   - Docker REST API 経由でクライアントからの要求に応答し、他のデーモンと対話
- Dockerオブジェクト
   - コンテナのデプロイをサポートするために、複数のオブジェクトを作成して構成
- Docker Hub
   - SaasのDockerコンテナレジストリ
   - 作成したコンテナイメージを格納して配布するために使用するレポジトリ
   - イメージ管理に使用される既定のパブリックレジストリ
- Host OS
   - Dockerエンジンが実行されるOS
   - Linux
      - DockerコンテナはホストOSカーネルを共有
   - Windows
      - コンテナOSが必要
- Container OS
   - パッケージ化されたイメージの一部であるOS
   - Host OSから分離されている、アプリケーションをデプロイして実行する環境
- Dockerfile
   - Dockerイメージをビルドして実行するために使用する命令が含まれているテキストファイル
- Bridge Network
   - 他のネットワーク構成を指定せずに起動した場合に、コンテナーに適用される既定の構成
   - 各コンテナにはIPアドレスとサブネットマスクが割り当てられ、ホスト名は規定でコンテナ名になる
   - 他のコンテナにIPアドレスを使ってアクセスできる
- Host Network
   - ホストネットワーク上でコンテナを直接実行できる
