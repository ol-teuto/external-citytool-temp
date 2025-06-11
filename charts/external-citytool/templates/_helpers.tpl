{{/*
Expand the name of the chart.
*/}}
{{- define "external-citytool.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "external-citytool.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "external-citytool.labels" -}}
helm.sh/chart: {{ include "external-citytool.chart" . }}
tenant: {{ .Values.tenant | quote }}
citytool: {{ .Values.citytool | quote }}
{{ include "external-citytool.selectorLabels" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "external-citytool.selectorLabels" -}}
app.kubernetes.io/name: {{ include "external-citytool.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
