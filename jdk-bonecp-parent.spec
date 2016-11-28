Name     : jdk-bonecp-parent
Version  : 0.8.0.RELEASE
Release  : 3
URL      : http://repo1.maven.org/maven2/com/jolbox/bonecp-parent/0.8.0.RELEASE/bonecp-parent-0.8.0.RELEASE.pom
Source0  : http://repo1.maven.org/maven2/com/jolbox/bonecp-parent/0.8.0.RELEASE/bonecp-parent-0.8.0.RELEASE.pom
Source1  : http://repo1.maven.org/maven2/com/jolbox/bonecp-parent/0.8.0.RELEASE/bonecp-parent-0.8.0.RELEASE.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/bonecp-parent.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/bonecp-parent.xml \
%{buildroot}/usr/share/maven-poms/bonecp-parent.pom \
%{buildroot}/usr/share/java/bonecp-parent.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/bonecp-parent.xml
/usr/share/maven-poms/bonecp-parent.pom
