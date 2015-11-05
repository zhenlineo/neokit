# Neo4j Driver Toolkit

Tools for downloading, managing and testing Neo4j servers.

- `neoget` - download and install Neo4j server packages
- `neoctl` - start and stop Neo4j servers
- `neorun` - run commands against one or more running servers


## Neoget
Neoget is a download script for fetching Neo4j server packages. To download the latest stable version of Neo4j, simply use:

```
neoget
```

If successful, the full name of the downloaded package will be displayed on the console immediately following the download.

To install a Neo4j package for the current user (into `${HOME}/.neokit`), use `-i`:

```
neoget -i
```

The `-x` option can be used to carry out a download only if the requested file does not already exist. The default is to overwrite files with the same name.

Specific versions can be obtained by providing the version numbers as arguments:

```
neoget -i 2.2.6 2.1.4
```

Alternatively, the pseudo-versions `milestone` and `nightly` can be used in place of an actual number.

The `-e` option forces a download of the Enterprise software; the Community edition (`-c`) is default:

```
neoget -e nightly
```

For a full help page, use `-h`:

```
neoget -h
```


## Neoctl
Neoctl is a controller for installed Neo4j packages (see `neoget -i`).

Once downloaded, a package must be unzipped before use. This can be achieved with the `unzip` command:

```
neoctl unzip 2.3.0
```

Note that a package may be unzipped as often as required. Doing so will overwrite any existing set of files, essentially resetting the database to factory conditions.

To start a server, use the `start` command:

```
neoctl start 2.3.0
```

Similarly, to stop a server, use the `stop` command:

```
neoctl stop 2.3.0
```


## Neorun
Neorun can be used to run a test script or other command against one or more running Neo4j servers. To do this, simply pass the command and the versions against which testing should occur. The command will be run once for each version listed:

```
neorun ./my-test-script.sh 2.3.0 2.2.6
```

Downloading and installing the required versions of Neo4j will be managed completely by this tool.
